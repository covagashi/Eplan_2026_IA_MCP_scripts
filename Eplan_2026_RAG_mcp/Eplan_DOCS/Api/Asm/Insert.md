# Insert

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert.html

---

Class for inserting different kinds of external data. The class Insert contains all methods for placing window macros or inserting window macros.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.Insert**

Syntax

**C#**



public class Insert

public ref class Insert


Example

Example shows how to use insert a window macro using Insert class

**C#**

```
Insert oInsert = new Insert();

oInsert.WindowMacro("$(MD_MACROS)\\BECK.KL1012.ema", 0, m_oTestProject.Pages[9], new PointD(70.0, 0.0), Insert.MoveKind.Relative);

```

Inserting page macro with overwriting some pages

**C#**

```
PageMacro oPageMacro = new PageMacro();

oPageMacro.Open(@"$(MD_MACROS)\1.emp", m_oTestProject);

//set new name to only two pages; rest pages will have default names

oPageMacro.Pages[1].Name = "=EB3+ET1/2";

oPageMacro.Pages[3].Name = "=EB3+ET1/3";

//overwrite 2., 3. and 4. page

Boolean[] arrOverwrite = new Boolean[5] { false, true, true, true, false };

new Insert().PageMacro(oPageMacro, m_oTestProject, arrOverwrite, PageMacro.Enums.NumerationMode.None);

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Insert Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~_ctor.html) | Default constructor |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ArePCTLoopsRenumbered](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~ArePCTLoopsRenumbered.html) | If true, renumbers PCT loop if name already exists. |
| Public Property | [ArePlanningObjectsInserted](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~ArePlanningObjectsInserted.html) | Indicates whether additional planning objects are inserted from macro into project. |
| Public Property | [ArePlanningObjectsStructureMerged](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~ArePlanningObjectsStructureMerged.html) | Indicates whether planning objects structure will be merged with existing nodes or renumbered and added. |
| Public Property | [PlanningSegment](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~PlanningSegment.html) | Determines the planning segment to which all function inserted from window macro on page will be assign. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~Dispose().html) | Destructor |
| Public Method | [PageMacro](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~PageMacro.html) | Overloaded. Inserts a page macro into project. User can specify which pages can be overwritten over existing pages in project. |
| Public Method | [PrePlanningMacro](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~PrePlanningMacro.html) | Inserts the pre-planning macros below the given structure segment. |
| Public Method | [SymbolMacro](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~SymbolMacro.html) | Overloaded. Places a symbol macro onto a given position of a page. You can set whether absolute coordinates or coordinates relative to its original position on the page should be used. |
| Public Method | [WindowMacro](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~WindowMacro.html) | Overloaded. Places a window macro onto a given position of a page. You can set whether absolute coordinates or coordinates relative to its original position on the page should be used. |


