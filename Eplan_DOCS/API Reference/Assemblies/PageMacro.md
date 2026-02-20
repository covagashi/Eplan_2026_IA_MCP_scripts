# PageMacro

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro.html

---

This class represents a page macro.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.MasterData.Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html)  
      **Eplan.EplApi.DataModel.MasterData.PageMacro**

Syntax

**C#**



public class PageMacro : Macro

public ref class PageMacro : public Macro

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [PageMacro Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro~_ctor.html) | Constructor. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [CountOfPages](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~CountOfPages.html) | Get the count of Pages in this macro (Inherited from [Eplan.EplApi.DataModel.MasterData.Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html)) |
| Public Property | [CustomLayerTable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~CustomLayerTable.html) | Gets layer table of custom layers (Inherited from [Eplan.EplApi.DataModel.MasterData.Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html)) |
| Public Property | [Description](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~Description.html) | Gets description in multiple languages (Inherited from [Eplan.EplApi.DataModel.MasterData.Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html)) |
| Public Property | [PageProperty](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~PageProperty.html) | Gets the property of the n-th page in this macro (Inherited from [Eplan.EplApi.DataModel.MasterData.Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html)) |
| Public Property | [Pages](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro~Pages.html) | Overridden. Returns pages, which are contained in the macro. |
| Public Property | [PlaceHolders](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro~PlaceHolders.html) | Returns all Eplan.EplApi.DataModel.Graphics.PlaceHolder contained in the macro. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro~Create.html) | Writes a macro file from the pages and then if there was at least one valid page, opens created macro. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~Dispose().html) | Destructor for deterministic finalization of PageMacro object. (Inherited from [Eplan.EplApi.DataModel.MasterData.Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html)) |
| Public Method | [Open](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro~Open(String,Project).html) | Opens a macro file and retrieves infomation from it. |
| Public Method | [StoreExternalFilesOfCurrentVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~StoreExternalFilesOfCurrentVariant.html) | Copies external files into project images directory (Inherited from [Eplan.EplApi.DataModel.MasterData.Macro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html)) |


