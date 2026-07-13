# EPLAN Script Basics

EPLAN scripts are C# source files compiled by EPLAN itself when loaded/run. No Visual Studio project needed; no API license needed.

## Minimal script

```csharp
using Eplan.EplApi.Scripting;
using Eplan.EplApi.Base;
using Eplan.EplApi.ApplicationFramework;

public class MyScript
{
    [Start]
    public void Function()
    {
        // your code
    }
}
```

## Entry-point attributes

### `[Start]` — run once via Utilities > Scripts > Run
```csharp
[Start]
public void Function() { }
```

### `[DeclareAction("Name")]` — registers a callable action
Loaded via "Load script". The action can then be called from toolbars, other scripts, the command line, or remote clients.
```csharp
[DeclareAction("MyCustomAction")]
public void Function() { }
```
Actions can receive and return parameters via `ActionCallingContext` and can declare an `int` return value (0 = success).

### `[DeclareEventHandler("event")]` — react to EPLAN events
```csharp
[DeclareEventHandler("onActionStart.String.XPrjActionProjectClose")]
public void OnClose() { }

// Wildcards work:
[DeclareEventHandler("onActionEnd.String.*")]
public void OnAnyActionEnd(IEventParameter iEventParameter) { }

// Framework events:
[DeclareEventHandler("Eplan.EplApi.OnUserPreCloseProject")]
public void BeforeProjectClose() { }
```
Common event patterns: `onActionStart.String.<ActionName>`, `onActionEnd.String.<ActionName>`.

### `[DeclareRegister]` / `[DeclareUnregister]` — script lifecycle
Run when the script is loaded/unloaded. This is where you add/remove ribbon tabs and context-menu entries.
```csharp
[DeclareRegister]
public void Register() { /* add ribbon tab */ }

[DeclareUnregister]
public void UnRegister() { /* remove ribbon tab */ }
```

## Deployment

- **One-shot**: Utilities > Scripts > Run (`[Start]` executes).
- **Persistent**: Utilities > Scripts > Load (registers `[DeclareAction]`/`[DeclareEventHandler]`/ribbon; survives until unloaded; auto-loads at startup once loaded).
- **From another script/app**: the `ExecuteScript` action with parameter `ScriptFile` (full path). This also works via Remote Client — the script runs inside EPLAN with full context.

## Scripting limitations vs API

- Scripts use a C# subset compiled by EPLAN. Partial classes across files, some newer C# language features, and designer-split WinForms files are not available — keep a form's `InitializeComponent` inline in the same class.
- No direct object-model manipulation of schematic items (that's API territory), but:
  - All **actions** are available (which covers most project operations).
  - Some **API namespaces work inside scripts**, notably `Eplan.EplApi.MasterData` (parts database) and `Eplan.EplApi.Base`. See `api-data-access.md`.
- `System.Windows.Forms`, `System.IO`, `System.Xml`, `System.Net.Http` are all usable — scripts can show dialogs, write files, and call HTTP services.

## Windows Forms in scripts

Keep everything in one class (no designer file):

```csharp
public partial class frmTemplate : System.Windows.Forms.Form
{
    private System.ComponentModel.IContainer components = null;

    protected override void Dispose(bool disposing)
    {
        if (disposing && (components != null)) components.Dispose();
        base.Dispose(disposing);
    }

    private void InitializeComponent()
    {
        this.SuspendLayout();
        this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
        this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
        this.ClientSize = new System.Drawing.Size(292, 273);
        this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
        this.Text = "Template";
        this.ResumeLayout(false);
    }

    public frmTemplate() { InitializeComponent(); }

    [Start]
    public void Function()
    {
        using (frmTemplate frm = new frmTemplate())
        {
            frm.ShowDialog();
        }
    }
}
```

## Debugging

- Log into EPLAN's system messages: `new BaseException("msg", MessageLevel.Message).FixMessage();` then open the system messages dialog (`SystemErrDialog` action).
- Write a plain log file for anything running unattended.
- A `MessageBox.Show` is fine for interactive debugging but never leave it in automation paths (it blocks headless runs).
