# Core EPLAN Classes

## PathMap — path variables

```csharp
using Eplan.EplApi.Base;

string projectPath = PathMap.SubstitutePath("$(PROJECTPATH)"); // project folder
string projectName = PathMap.SubstitutePath("$(PROJECTNAME)"); // name only
string fullProject = PathMap.SubstitutePath("$(P)");           // full .elk path
```

| Variable | Meaning |
|---|---|
| `$(PROJECTPATH)` | Project directory |
| `$(PROJECTNAME)` | Project name |
| `$(P)` | Full project path (.elk) |
| `$(TMP)` | Temp directory |
| `$(MD_SCRIPTS)` | Scripts master-data dir |
| `$(MD_DOCUMENTS)` | Documents master-data dir (common in part document links) |

Resolve any raw string that may contain variables:
```csharp
private string ResolvePath(string rawPath)
{
    if (string.IsNullOrEmpty(rawPath) || !rawPath.Contains("$(")) return rawPath;
    try { return PathMap.SubstitutePath(rawPath); } catch { return rawPath; }
}
```

## Progress — progress bars

```csharp
Progress oProgress = new Progress("SimpleProgress");   // or "EnhancedProgress"
oProgress.SetAllowCancel(true);
oProgress.SetAskOnCancel(true);
oProgress.SetNeededSteps(3);            // or BeginPart(100, "")
oProgress.SetTitle("My operation");
oProgress.ShowImmediately();

if (!oProgress.Canceled())
{
    oProgress.SetActionText("Step 1");
    oProgress.Step(1);
}
oProgress.EndPart(true);                // ALWAYS call, use finally
```

## Decider — EPLAN-native dialogs

```csharp
new Decider().Decide(
    EnumDecisionType.eOkDecision,
    "Message", "Title",
    EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
```
For list selection there is `ListSelectDecisionContext`. `System.Windows.Forms.MessageBox` is also fine in interactive scripts.

## Settings — read/write EPLAN settings

```csharp
var oSettings = new Eplan.EplApi.Base.Settings();

oSettings.SetStringSetting("USER.TrDMProject.UserData.Identification", "TEST", 0);
oSettings.SetBoolSetting("USER.EnfMVC.ContextMenuSetting.ShowExtended", true, 0);
oSettings.SetNumericSetting("USER.SYSTEM.GUI.LAST_PROJECTS_COUNT", 11, 0);

string s = oSettings.GetStringSetting("USER.TrDMProject.UserData.Longname", 0);
bool b   = oSettings.GetBoolSetting("USER.XUserSettingsGui.UseLoginName", 0);
int n    = oSettings.GetNumericSetting("USER.MF.PREVIEW.MINCOLWIDTH", 0);
```
Setting paths are hierarchical (`USER.*`, `STATION.*`, `PROJECT.*`). Find exact paths via the RAG or by exporting settings (`XSettingsExport`/`XSettingsImport`).

## MultiLangString — multilanguage texts

```csharp
MultiLangString name = new MultiLangString();
name.AddString(ISOCode.Language.L_en_US, "My Tab");
name.AddString(ISOCode.Language.L_de_DE, "Mein Tab");
```

Raw multilang values from properties serialize like `en_US@Text;es_ES@Texto` (sometimes wrapped in `{{ }}`). Parsing pattern (prefer English, fall back to first):

```csharp
private string ParseMultiLang(string rawText)
{
    if (string.IsNullOrEmpty(rawText)) return "";
    string fallback = "", english = "";
    foreach (string part in rawText.Split(new[] { ';' }, StringSplitOptions.RemoveEmptyEntries))
    {
        string val = part;
        int atIdx = part.IndexOf('@');
        if (atIdx >= 0)
        {
            string lang = part.Substring(0, atIdx).ToLower();
            val = part.Substring(atIdx + 1).Replace("{{", "").Replace("}}", "").Trim();
            if (string.IsNullOrEmpty(fallback)) fallback = val;
            if (lang.StartsWith("en")) english = val;
        }
        else
        {
            val = part.Replace("{{", "").Replace("}}", "").Trim();
            if (string.IsNullOrEmpty(fallback)) fallback = val;
        }
    }
    string result = !string.IsNullOrEmpty(english) ? english : fallback;
    return string.IsNullOrEmpty(result) ? rawText.Replace("{{", "").Replace("}}", "").Trim() : result;
}
```

## Ribbon and context menus (EPLAN 2022+)

Classic menu bar is gone since 2022 — use `Eplan.EplApi.Gui.RibbonBar` inside `[DeclareRegister]`:

```csharp
using Eplan.EplApi.Gui;

[DeclareRegister]
public void Register()
{
    RibbonBar ribbonBar = new RibbonBar();
    RibbonTab tab = ribbonBar.GetTab(TAB_NAME, true) ?? ribbonBar.AddTab(TAB_NAME);

    RibbonCommandGroup group = tab.AddCommandGroup("My group");
    group.AddCommand("My action", "MyActionName", new RibbonIcon(CommandIcon.Accumulator));

    // Custom icon from SVG + multilang labels/tooltips:
    RibbonIcon icon = ribbonBar.AddIcon(@"C:\icons\my.svg");
    group.AddCommand(commandText, "MyActionName", tooltip, description, icon);
}

[DeclareUnregister]
public void UnRegister()
{
    RibbonTab tab = new RibbonBar().GetTab(TAB_NAME, true);
    if (tab != null) tab.Remove();
}
```
`TAB_NAME` is a `MultiLangString`. There is also `ContextMenu`/`ContextMenuLocation` for right-click menus.

## System messages

```csharp
// Emit into EPLAN's system message list (visible in the messages dialog):
new BaseException("Something happened", MessageLevel.Message).FixMessage();
new BaseException("Warning text", MessageLevel.Warning).FixMessage();
new BaseException("Error text", MessageLevel.Error).FixMessage();

// Show the dialog:
new CommandLineInterpreter().Execute("SystemErrDialog");
```

### Reading system messages incrementally (bookmark pattern)
```csharp
private static int lastBookmarkID = 0;

[DeclareEventHandler("onActionEnd.String.*")]
public void OnActionEnd(IEventParameter iEventParameter)
{
    SysMessagesCollection colSysMsg = new SysMessagesCollection(lastBookmarkID, MessageLevel.Error);
    if (colSysMsg.Count > 0)
    {
        BaseException last = colSysMsg.Cast<BaseException>().LastOrDefault();
        // ...process...
        lastBookmarkID = colSysMsg.BookmarkIDEnd;   // advance bookmark, avoids reprocessing
    }
}
```
