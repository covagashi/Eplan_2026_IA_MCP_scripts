# Synchronize

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize.html

---

Class providing functionality for synchronizing project and system master data and synchronizing properties between different representation types.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.Synchronize**

Syntax

**C#**



public class Synchronize

public ref class Synchronize

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Synchronize Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~_ctor.html) | Default constructor |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CablingToAllConnectionTypes](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~CablingToAllConnectionTypes.html) | Synchronization from 'cabling' connection data onto all other connection types (multi-line, panellayout 3D, single-line) |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~Dispose().html) | Destructor |
| Public Method | [MultilineToAllConnectionTypes](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~MultilineToAllConnectionTypes.html) | Synchronization from 'multi-line' connection data onto all other connection types (panellayout 3D, cabling, single-line) |
| Public Method | [MultilineToSinglelineAndOverview](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~MultilineToSinglelineAndOverview.html) | Synchronization from 'multi-line' data onto 'single-line' and 'overview' data. |
| Public Method | [OverviewToMultilineAndSingleline](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~OverviewToMultilineAndSingleline.html) | Synchronization from 'overview' data onto 'single-line' and 'multi-line' data. |
| Public Method | [PanelLayout3DToAllConnectionTypes](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~PanelLayout3DToAllConnectionTypes.html) | Synchronization from 'panellayout 3D' connection data onto all other connection types (multi-line, cabling, single-line) |
| Public Method | [Parts](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~Parts.html) | Overloaded. Synchronizes the parts in the project to the parts master database. Updates parts database. This method corresponds with the EPLAN functionality in the ribbon "Master data \> Parts \> Synchronize". Additionally the user can specify, whether parts, which are already existing in the parts database, should be modified. |
| Public Method | [PartsDatabaseItemToProject](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~PartsDatabaseItemToProject.html) | Overloaded. Synchronizes the database items (like parts, manufactures addresses, etc.) stored in the project with the items in the parts master database. This function updates items inside project; items in the database are not changed. This method corresponds with the EPLAN functionality in the ribbon "Master data \> Parts \> Synchronize". |
| Public Method | [PartToProject](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~PartToProject.html) | Synchronizes the specified parts inside the project with the parts in the parts master database. Updates parts inside project. Parts in the database are not changed. This method corresponds with the EPLAN functionality in the ribbon "Master data \> Parts \> Synchronize" for selected parts. |
| Public Method | [PartToSystem](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~PartToSystem.html) | Overloaded. Synchronizes the specified parts into the parts master database. Updates parts database. Parts in the project are not changed. This method corresponds with the EPLAN functionality in the ribbon "Master data \> Parts \> Synchronize" for selected parts. |
| Public Method | [PIDToOtherPlacementTypes](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~PIDToOtherPlacementTypes.html) | Synchronization from PID data onto other representations. Corresponds to the Tools' -> 'Synchronization' -> 'PI diagram --> all representation types' ribbon item. |
| Public Method | [SinglelineToMultilineAndOverview](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~SinglelineToMultilineAndOverview.html) | Synchronization from 'single-line' data onto 'multi-line' and 'overview' data. |


