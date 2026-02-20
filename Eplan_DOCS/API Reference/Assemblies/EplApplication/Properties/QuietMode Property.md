# QuietMode Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~QuietMode.html

---

Quiet mode in which Eplan P8 has been started.

Syntax

**C#**



public EplApplication.QuietModes QuietMode {get; set;}

public:

property EplApplication.QuietModes QuietMode {

   EplApplication.QuietModes get();

   void set (    EplApplication.QuietModes value);

}


Remarks

Methods: [OpenProjectDlg](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~OpenProjectDlg.html), [ShowSystemErrorDlg](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~ShowSystemErrorDlg.html), [ShowSettingDlg](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~ShowSettingDlg.html), [ShowApiAddInDialog](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~ShowApiAddInDialog.html), [ShowPartSelectionDialog(String,String,PartsDatabaseItemType)](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~ShowPartSelectionDialog(String,String,PartsDatabaseItemType).html) ignores QuietMode and always shows dialog. API by default hides some dialogs which are visible in GUI. Those dialogs will be shown in API offline application after using [SetMainFrame](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~SetMainFrame.html) method.
