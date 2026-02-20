# Mate.Enums.RotationType

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate+Enums+RotationType.html

---

Possible types of forced rotation when the snap is done.

Syntax

**C#**



public enum Mate.Enums.RotationType : System.Enum

public enum class Mate.Enums.RotationType : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Fix** | 1 | No rotation. |
| **Free** | 2 | No limits of rotation. |
| **R180** | 5 | Only angles of 0 and 180 degrees are allowed. |
| **R45** | 3 | Only angles of 0,45,90,135 degrees are allowed. |
| **R90** | 4 | Only angles of 0,90,180,270 degrees are allowed. |
| **Undefined** | 0 | Undefined. |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.DataModel.E3D.Mate.Enums.RotationType**
