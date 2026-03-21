# SetMainFrame Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~SetMainFrame.html

---

Sets a new Mainframe for API offline program. API offline program will show all dialogs which are normally hidden in add-ins. It is possible to hide such dialogs using [ResetQuietMode](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~ResetQuietMode.html) method.

Syntax

**C#**



public void SetMainFrame( 

   IntPtr pMainWnd

)

public:

void SetMainFrame( 

   IntPtr pMainWnd

)


#### Parameters

*pMainWnd*

Example

**C#**

```
p.e. form1 is a System.Windows.Forms.Form

Eplan.EplApi.System.EplApplication app = new Eplan.EplApi.System.EplApplication();

app.SetMainFrame(form1.Handle);
```
