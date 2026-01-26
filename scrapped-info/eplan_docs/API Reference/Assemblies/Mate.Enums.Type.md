# Mate.Enums.Type

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate+Enums+Type.html

---

Types of mates.

Syntax

**C#**



public enum Mate.Enums.Type : System.Enum

public enum class Mate.Enums.Type : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Face** | 0 | Mate which occurs as surface. |
| **Fix** | 3 | Mate which occurs as point. Objects can be snapped on this point, but only in a fix position (rotation not allowed). |
| **FreeRotation** | 4 | Mate which occurs as point. Objects can be snapped on this point - rotation of objects is allowed. |
| **Grid** | 5 | Mate which occurs as grid. |
| **GridLine** | 6 | Mate which occurs as line of grid. Objects can be snapped along the line only on discrete positions (grid intersection points). |
| **Line** | 2 | Mate which occurs as line. |
| **Point** | 1 | Mate which occurs as point. |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.DataModel.E3D.Mate.Enums.Type**
