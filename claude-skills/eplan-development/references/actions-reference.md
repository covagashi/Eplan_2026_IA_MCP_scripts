# Executing Actions

Actions are EPLAN's command surface — nearly everything the UI does is an action. If you're unsure of a name or parameter, **query the RAG first** (`POST https://rag2026.covaga.xyz/search`), including "hidden actions" not in the official docs.

## Basic execution

```csharp
using Eplan.EplApi.ApplicationFramework;

CommandLineInterpreter oCLI = new CommandLineInterpreter();
oCLI.Execute("gedRedraw");
```

## With parameters (`ActionCallingContext`)

```csharp
using (ActionCallingContext acc = new ActionCallingContext())
{
    acc.AddParameter("TYPE", "PROJECT");
    acc.AddParameter("CONFIGSCHEME", "Standard");
    new CommandLineInterpreter().Execute("compress", acc);
}
```

## Reading values back from an action

```csharp
ActionCallingContext oACC = new ActionCallingContext();
oACC.AddParameter("TYPE", "PAGES");
new CommandLineInterpreter().Execute("selectionset", oACC);
string pagesString = string.Empty;
oACC.GetParameter("PAGES", ref pagesString);
string[] pages = pagesString.Split(';');   // "=PRJ+LOC/PAGE" identifiers
```

## Action catalog (verified parameter sets)

### backup — project backup
```csharp
acc.AddParameter("BACKUPMEDIA", "DISK");
acc.AddParameter("ARCHIVENAME", "MyProject_Backup_2026-07-13");
acc.AddParameter("DESTINATIONPATH", @"C:\Backups\");
acc.AddParameter("PROJECTNAME", PathMap.SubstitutePath("$(P)")); // full project path
acc.AddParameter("TYPE", "PROJECT");
oCLI.Execute("backup", acc);
```

### export — PDF export
```csharp
acc.AddParameter("TYPE", "PDFPROJECTSCHEME");
acc.AddParameter("EXPORTFILE", PathMap.SubstitutePath("$(PROJECTPATH)") + @"\" + projectName);
oCLI.Execute("export", acc);
```
Other TYPE values exist for DXF/DWG, images, etc. — check RAG for the scheme names.

### label — labeling / output files (Excel etc.)
```csharp
acc.AddParameter("CONFIGSCHEME", "Summarized parts list");
acc.AddParameter("DESTINATIONFILE", filename);
acc.AddParameter("LANGUAGE", "en_EN");
acc.AddParameter("SHOWOUTPUT", "1");
oCLI.Execute("label", acc);
```

### selectionset — get current selection
`TYPE` = `PAGES`, `PROJECT`, `DEVICES`... returns parameter of the same name with `;`-separated identifiers.

### edit — open/navigate to a page or device
```csharp
acc.AddParameter("PAGENAME", page);          // page identifier from selectionset
oCLI.Execute("edit", acc);
```

### Page properties — read a property of the open page
```csharp
acc.AddParameter("PropertyId", "11006");     // page type
oCLI.Execute("XEsGetPagePropertyAction", acc);
string value = ""; acc.GetParameter("PropertyValue", ref value);
```

### Common project/report actions
| Action | Purpose | Notes |
|---|---|---|
| `compress` | Compress project | `TYPE`, `CONFIGSCHEME`, `FILTERSCHEME` |
| `generate` | Generate connections/cables | |
| `reports` | Generate/update reports | |
| `partslist` / `devicelist` | Output part/device lists | |
| `print` | Print | |
| `import` / `export` | Import/export data | many TYPE variants |
| `XSettingsImport` | Import settings XML | `XMLFile` param |
| `ProjectAction` | Run an action against a specific project | `PROJECTNAME` |
| `XPrjActionProjectClose` | Close project | |
| `XGedClosePage` | Close open page in graphical editor | |
| `XPmExternalDeletePages` | Delete selected pages | destructive — pair with QuietMode carefully |
| `gedRedraw` | Redraw graphical editor | |
| `UpdateSegmentsFilling` | Update segment filling | |
| `ExecuteScript` | Run a script file | `ScriptFile` = full path; key for remote automation |
| `SystemErrDialog` | Show system messages dialog | |
| `CogineerGenerateFromExcelAction` | Cogineer: generate project from Excel | see remoting.md |

### Suppressing dialogs during batch operations
```csharp
using (var qm = new QuietModeStep(QuietModes.ShowNoDialogs))
{
    new CommandLineInterpreter().Execute("XPmExternalDeletePages");
}
```

## Iterating selected pages (complete pattern)

```csharp
[Start]
public void Action()
{
    var pages = GetPages();
    Progress progress = new Progress("EnhancedProgress");
    progress.SetTitle("Processing pages");
    progress.SetAllowCancel(true);
    progress.ShowImmediately();
    progress.SetNeededSteps(pages.Length + 1);
    try
    {
        foreach (var page in pages)
        {
            progress.SetActionText(page);
            progress.Step(1);
            // edit page, read property, act...
        }
    }
    catch (Exception ex)
    {
        MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
    }
    finally
    {
        progress.EndPart(true);
    }
}
```
