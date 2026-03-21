# Macro

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro.html

---

This is a base class for: [PageMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro.html), [WindowMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro.html), [SymbolMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolMacro.html). Class provides basic functionality for macros. This type can be used in order to declare a variable or parameter that holds any type of macro.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.MasterData.Macro**  
      [Eplan.EplApi.DataModel.MasterData.PageMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro.html)  
      [Eplan.EplApi.DataModel.MasterData.WindowMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro.html)

Syntax

**C#**



public class Macro

public ref class Macro


Remarks

Especially in offline programs, please make sure to clean up any macro objects before calling EplAppication.Exit(). The finalizer of macros needs the API still to be initialized!

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Macro Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~_ctor.html) | Constructor. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [CountOfPages](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~CountOfPages.html) | Get the count of Pages in this macro |
| Public Property | [CustomLayerTable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~CustomLayerTable.html) | Gets layer table of custom layers |
| Public Property | [Description](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~Description.html) | Gets description in multiple languages |
| Public Property | [PageProperty](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~PageProperty.html) | Gets the property of the n-th page in this macro |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~Dispose().html) | Destructor for deterministic finalization of Macro object. |
| Public Method | [StoreExternalFilesOfCurrentVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~StoreExternalFilesOfCurrentVariant.html) | Copies external files into project images directory |


