# ProjectManager.DatabaseVersion.Status

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager+DatabaseVersion+Status.html

---

Enum used for project database status.

Syntax

**C#**



public enum ProjectManager.DatabaseVersion.Status : System.Enum

public enum class ProjectManager.DatabaseVersion.Status : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **IsCompatible** | 1 | Data is compatible (at most the minor version was changed) |
| **IsIncompatible** | 2 | Data is incompatible to the current version (and not convertible) |
| **NeedsUpgrade** | 0 | Data is incompatible to the current version (but convertible) |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.DataModel.ProjectManager.DatabaseVersion.Status**
