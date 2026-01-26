# SubProject.SubProjectStatus

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.SubProject+SubProjectStatus.html

---

Possible statuses of subproject.

Syntax

**C#**



public enum SubProject.SubProjectStatus : System.Enum

public enum class SubProject.SubProjectStatus : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Revisioned** | 5 | Project is revisioned. |
| **SubProjectFiledOff** | 3 | Subproject is filed off. (Exported) |
| **SubProjectNotEditable** | 4 | The subproject is not an editable project (\*.elk), it cannot be filed off. |
| **SubProjectStored** | 2 | Subproject is stored. (Imported) |
| **Unknown** | 0 | Status is unknown. |
| **WorkingSectionOverlaps** | 1 | Defined working section overlaps - parts of this defined working section are also contained in other defined working sections. Filing off is not possible. |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.EServices.SubProject.SubProjectStatus**
