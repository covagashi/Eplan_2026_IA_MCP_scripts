# Critical Pitfalls

These are the failure modes that actually bite in production. Read before writing any multi-step EPLAN automation.

## 1. The command-blocking issue (message loop)

**Symptoms**: an EPLAN command (`reports`, `translate`, `backup`…) completes its work, but your C# code hangs after `oCLI.Execute()`; subsequent log lines never run; the process looks frozen while EPLAN itself is fine.

**Root cause**: EPLAN commands are **pseudo-asynchronous** — they run in EPLAN's context and need an active Windows message loop to signal completion. Without one, `Execute()` never returns.

**Solution**: keep a secondary thread pumping message monitoring while the main thread runs commands sequentially:

```csharp
bool continueMonitoring = true;
Thread monitorThread = new Thread(() =>
{
    while (continueMonitoring)
    {
        _messageMonitor.MonitorMessages();   // keeps the message loop alive
        Thread.Sleep(3500);
    }
});
monitorThread.Start();

try
{
    // Main thread: run EPLAN operations SEQUENTIALLY
    UpdateConnections(projectName);
    GenerateReport(projectName);
    Translate(projectName);
    Compress(projectName);
    BackupProject(projectName, exportDir, comment);
}
finally
{
    continueMonitoring = false;
    monitorThread.Join();       // never leave orphan threads
}
```

Non-solutions that were tried and failed: `Task.Wait()` with timeout, extra action parameters, sleeps/delays. The monitor thread is architectural, not a workaround.

## 2. Sequential execution model

All EPLAN operations against one instance are **strictly sequential** — each action must fully finish before the next starts (reports need synchronized data; backup needs compress done; etc.). Never parallelize actions against the same EPLAN instance. The only legitimate parallel thread is the message monitor above (it doesn't run actions).

## 3. `using` / `Dispose` discipline

`ActionCallingContext`, `EplanRemoteClient`, streams, forms — anything `IDisposable` — must be disposed even on exception. Missed disposals leak native resources and can wedge remoting connections.

```csharp
// Preferred:
using (ActionCallingContext acc = new ActionCallingContext())
{
    ...
} // disposed even if an exception is thrown

// Stacked:
using (var r1 = new Resource1())
using (var r2 = new Resource2())
{ ... }
```
For long-lived clients (e.g. a WPF app holding an `EplanRemoteClient`), implement the full `IDisposable` pattern: `Dispose()` → disconnect → stop process if you own it → dispose client → null it.

## 4. Error handling rules

```csharp
// ❌ NEVER
try { ... } catch { }

// ✅ Inside EPLAN scripts — surface into system messages:
catch (Exception ex)
{
    new BaseException("Error: " + ex.Message, MessageLevel.Error).FixMessage();
}

// ✅ In external apps — log everything remoting gives you:
catch (Exception ex)
{
    _logger.LogError($"[CONNECT] {ex.GetType().FullName}: {ex.Message}");
    if (ex.InnerException != null)
        _logger.LogError($"[CONNECT] Inner: {ex.InnerException.Message}");
}
```
- In batch loops (parts DB scans, page iterations): catch per item, log the item id, continue.
- In interactive scripts: `MessageBox.Show(ex.Message, "Error", ...)` is acceptable; never in headless paths.

## 5. Progress bars must always end

`Progress.EndPart(true)` in `finally`, or EPLAN's UI is left with a stuck progress dialog. Check `Canceled()` inside loops when `SetAllowCancel(true)`.

## 6. Long-running work completion detection

Long remote scripts give weak completion signals. Robust patterns:
- Script writes a sentinel file / final artifact (ZIP) → external app polls the folder (timer, 2 s).
- Script posts status to a local HTTP/SignalR endpoint (see integration-patterns.md).

## 7. File writing from scripts

- Overwrite checks before writing user-facing outputs (`File.Exists` → ask).
- Timestamped names for backups: `name_Backup_yyyy-MM-dd_hh-mm-ss`.
- Create directories before use: `Directory.CreateDirectory(dir)` is idempotent.
- EPLAN examples traditionally use `Encoding.Unicode` for text files it re-reads; use UTF-8 for anything consumed by other tools.

## 8. Miscellaneous

- Dialogs kill headless automation — suppress with `QuietModeStep(QuietModes.ShowNoDialogs)` around dialog-prone actions, and never `ShowDialog()` in automation paths.
- Action names and parameters are case-sensitive strings with zero compile-time checking — a typo fails silently or at runtime. Verify against the RAG.
- Ports are dynamic; process name is `W3u`; EPLAN 2025 needs "Remote Client Access" enabled (see remoting.md).
