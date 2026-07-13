# Integration Patterns — Connecting EPLAN to External Systems

EPLAN scripts can use `System.Net.Http` and even SignalR clients, which enables event-driven bridges between EPLAN and web services, dashboards, or queues.

## HTTP client from a script

```csharp
using System.Net.Http;

// Reuse a single static client (avoid socket exhaustion):
private static readonly HttpClient client = new HttpClient();

// GET
HttpResponseMessage response = client.GetAsync("http://localhost:8000").Result;
if (response.IsSuccessStatusCode)
{
    string content = response.Content.ReadAsStringAsync().Result;
}

// POST
var content = new StringContent(json, Encoding.UTF8, "application/json");
HttpResponseMessage resp = client.PostAsync(url, content).Result;
```
Note: scripts run synchronously — `.Result`/`.Wait()` on HTTP calls is the established pattern here (there is no async entry point). Keep timeouts short so a dead server doesn't hang EPLAN.

## Forwarding EPLAN system errors to a server (event-driven)

Complete production pattern — an event handler that captures new error messages after every action and ships them out, with a local file fallback:

```csharp
public class SystemMessageLogger
{
    private static readonly HttpClient client = new HttpClient();
    private const string SERVER_URL = "http://localhost:8000/log";
    private const string LOG_FILE_PATH = @"C:\Temp\EplanErrorLog.txt";
    private static int lastBookmarkID = 0;

    [DeclareEventHandler("onActionEnd.String.*")]
    public void OnActionEnd(IEventParameter iEventParameter)
    {
        try
        {
            var colSysMsg = new SysMessagesCollection(lastBookmarkID, MessageLevel.Error);
            if (colSysMsg.Count > 0)
            {
                BaseException last = colSysMsg.Cast<BaseException>().LastOrDefault();
                if (last != null)
                {
                    SendMessageToServer("Error: " + last.ToString()).Wait();
                }
                lastBookmarkID = colSysMsg.BookmarkIDEnd;   // only new messages next time
            }
        }
        catch (Exception ex)
        {
            WriteLocalLog("Handler error: " + ex);   // never let the handler throw
        }
    }

    private async Task SendMessageToServer(string message)
    {
        try
        {
            var content = new StringContent(message, Encoding.UTF8, "text/plain");
            var response = await client.PostAsync(SERVER_URL, content);
            if (!response.IsSuccessStatusCode)
                WriteLocalLog("Send failed: " + response.StatusCode);
        }
        catch (Exception ex) { WriteLocalLog("Send exception: " + ex); }
    }

    private void WriteLocalLog(string message)
    {
        try
        {
            using (StreamWriter sw = File.AppendText(LOG_FILE_PATH))
                sw.WriteLine(DateTime.Now + ": " + message);
        }
        catch { /* last resort — nowhere left to log */ }
    }
}
```
Key details: bookmark-based incremental reads, `.Wait()` on send (script context), file fallback so failures are never invisible, and the handler itself never throws.

## Exposing EPLAN actions over HTTP

Inverse direction: a lightweight local server (Python/ASP.NET) receives requests and a loaded EPLAN script polls it — or the external app simply uses the Remote Client (`ExecuteAction`) which is the cleaner path. Prefer Remote Client for command-and-control; use HTTP polling only when the client cannot reference EPLAN DLLs.

## SignalR — real-time bidirectional messaging

For live dashboards (EPLAN progress → browser) an ASP.NET Core SignalR hub works with an EPLAN-side script acting as a SignalR client posting status, and browsers subscribing to the hub. Architecture:

- **Hub app** (external, ASP.NET Core): `Hub` subclass + `wwwroot` page with the JS client.
- **EPLAN script**: posts to a controller endpoint (`MessagesController`) or connects with the SignalR .NET client; sends status per pipeline step.
- Browsers get push updates without polling.

Use when several observers need live progress; otherwise plain HTTP POST + file sentinel (pitfalls.md §6) is simpler.

## Generating self-contained HTML tools from scripts

A powerful pattern for data deliverables: a script scans EPLAN data (e.g. parts DB) and emits a **single self-contained HTML file** with the dataset embedded as JSON plus client-side JS for filtering/matching/export (JSZip, ExcelJS via CDN). Users get an interactive tool with zero infrastructure. Pair it with a JSON export of the same data for machine consumption.
