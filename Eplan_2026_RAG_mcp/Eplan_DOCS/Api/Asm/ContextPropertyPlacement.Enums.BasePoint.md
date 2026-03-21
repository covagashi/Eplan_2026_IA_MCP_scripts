# ContextPropertyPlacement.Enums.BasePoint

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement+Enums+BasePoint.html

---

Enumeration of BasePoint type There can be set only several values for some objects. For example: values: InsertionPoint, UpperLeft, UpperCenter, UpperRight, MiddleLeft, MiddleCenter, MiddleRight, LowerLeft, LowerCenter, LowerRight are available for objects: BOX, LOCATIONBOX, MACROBOX, SHIELDING. values: InsertionPoint, CableUpperLeft, CableCenter, CableLowerRight are available for object: CABLE. etc.

Syntax

**C#**



public enum ContextPropertyPlacement.Enums.BasePoint : System.Enum

public enum class ContextPropertyPlacement.Enums.BasePoint : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **AutoY** | 17 | Base point: Fixed Y-Position |
| **CableCenter** | 13 | Base point: Center - for cable objects |
| **CableLowerRight** | 15 | Base point: Lower right - for cable objects |
| **CableUpperLeft** | 14 | Base point: Upper left - for cable objects |
| **InsertionPoint** | 0 | Default value |
| **LowerCenter** | 6 | Base point: Lower center - for box objects |
| **LowerLeft** | 3 | Base point: Lower left - for box objects |
| **LowerRight** | 4 | Base point: Lower right - for box objects |
| **MiddleCenter** | 9 | Base point: Middle center - for box objects |
| **MiddleLeft** | 7 | Base point: Middle left - for box objects |
| **MiddleRight** | 8 | Base point: Middle right - for box objects |
| **Terminal** | 16 | Base point: Terminal - for some objects |
| **UpperCenter** | 5 | Base point: Upper center - for box objects |
| **UpperLeft** | 1 | Base point: Upper left - for box objects |
| **UpperRight** | 2 | Base point: Upper right - for box objects |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.DataModel.ContextPropertyPlacement.Enums.BasePoint**
