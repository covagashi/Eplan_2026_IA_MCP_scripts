# FileSelectDecisionContext

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.FileSelectDecisionContext.html

---

This class can be used for an standard eplan decider

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.FileSelectDecisionContext**

Syntax

**C#**



public class FileSelectDecisionContext

public ref class FileSelectDecisionContext


Example

Example of using Decider class with a FileSelectDecisionContext :

**C#**

```


FileSelectDecisionContext fileContext = new FileSelectDecisionContext("ExlSheetSelector", EnumDecisionReturn.eCANCEL);

fileContext.Title = "Select Excel file";

fileContext.AllowMultiSelect = false;

fileContext.DefaultExtension = "xls";

fileContext.AddFilter("Excel 97 files (*.xls)", "*.xls");

fileContext.AddFilter("Excel files (*.xlsx)", "*.xlsx");

fileContext.AddFilter("Fenstermakro, Symbolmakro (*.ema, *.ems)", "*.ema;*.ems");

fileContext.AddFilter("All files (*.*)", "*.*");

Decider oDecision = new Decider();

EnumDecisionReturn eAnswer = oDecision.Decide(fileContext);

if (eAnswer != EnumDecisionReturn.eOK)

{

    return true;

}

string sExlFile = fileContext.GetFiles()[0];

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [FileSelectDecisionContext Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.FileSelectDecisionContext~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AllowMultiSelect](Eplan.EplApi.Baseu~Eplan.EplApi.Base.FileSelectDecisionContext~AllowMultiSelect.html) | Set or get the flag for multi selection. |
| Public Property | [CustomDefaultPath](Eplan.EplApi.Baseu~Eplan.EplApi.Base.FileSelectDecisionContext~CustomDefaultPath.html) | Set or get the CustomDefaultPath. This is the path the File Select Dialog opens first. The second time the path is used the user has selected the last time. Then the context menu "Set to standard" will select this path again. |
| Public Property | [DefaultExtension](Eplan.EplApi.Baseu~Eplan.EplApi.Base.FileSelectDecisionContext~DefaultExtension.html) | The default extension of the files to select. |
| Public Property | [DefaultFilename](Eplan.EplApi.Baseu~Eplan.EplApi.Base.FileSelectDecisionContext~DefaultFilename.html) | The default name of a file. |
| Public Property | [OpenFileFlag](Eplan.EplApi.Baseu~Eplan.EplApi.Base.FileSelectDecisionContext~OpenFileFlag.html) | Set or get the openfileflag. Set this flag when you want to open a file Do not set it when you want to save a file. |
| Public Property | [Title](Eplan.EplApi.Baseu~Eplan.EplApi.Base.FileSelectDecisionContext~Title.html) | The title for the decider. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddFilter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.FileSelectDecisionContext~AddFilter.html) | Add a filter which files are shown. When the user selects one filter in the decider dialog, only files of this type are displayed. |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.FileSelectDecisionContext~Dispose().html) | Destructor for deterministic finalization of FileSelectDecisionContext object. |
| Public Method | [GetFiles](Eplan.EplApi.Baseu~Eplan.EplApi.Base.FileSelectDecisionContext~GetFiles.html) | Get all the files the user has selected in the decider dialog. |


