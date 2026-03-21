# ProjectSections

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSections.html

---

Class to manage project sections. Objects of this class are returned by a project's [Project.Sections](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Sections.html) property.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.ProjectSections**

Syntax

**C#**



public class ProjectSections

public ref class ProjectSections


Example

**C#**

```
ProjectSections sections = _CurrentProject.Sections;

sections.State = ProjectSections.Enums.State.Enabled;

sections.ActiveScheme = "Trade_Fluid_power";

(...)

sections.ActiveScheme = "Trade_Electrical_engineering";
```

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ActiveScheme](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSections~ActiveScheme.html) | Gets/Sets active working section scheme for current user. |
| Public Property | [AvailableSchemes](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSections~AvailableSchemes.html) | Gets all schemes for working sections. |
| Public Property | [State](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSections~State.html) | Gets/Sets whether sections are active (i.e. visible) for the currently logged-in user |


