# ProjectManager.CopyMode

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager+CopyMode.html

---

Enum used in CopyProject() method. Determines what should be copied.

Syntax

**C#**



public enum ProjectManager.CopyMode : System.Enum

public enum class ProjectManager.CopyMode : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **All** | 0 | Copies all |
| **OnlyLogic** | 3 | Copies only logic |
| **OnlyProjecthead** | 2 | Copies only project head |
| **Snapshot** | 32768 | Copies all, but copy is done in non-exclusive mode |
| **WithoutEvaluation** | 1 | Copies without evaluation |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.DataModel.ProjectManager.CopyMode**
