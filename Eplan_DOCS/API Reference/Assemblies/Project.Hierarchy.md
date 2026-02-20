# Project.Hierarchy

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project+Hierarchy.html

---

Hierarchy level of the device structure

Syntax

**C#**



public enum Project.Hierarchy : System.Enum

public enum class Project.Hierarchy : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Document** | 5 | Document type (&) |
| **Functional** | 0 | Functional assignment (==) |
| **Installation** | 4 | Higher level function number |
| **Location** | 3 | Mounting location (+) |
| **NotSpecified** | -1 | not specified (used to indicate that project sections are not enabled) |
| **Place** | 2 | Installation site (++) |
| **Plant** | 1 | Higher-level function (=) |
| **Product** | 7 | Product |
| **UserDef** | 6 | User-defined (#) |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.DataModel.Project.Hierarchy**
