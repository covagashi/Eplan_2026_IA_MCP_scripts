# SymbolReference.PointVariant

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+PointVariant.html

---

Configuration types to select different variants for point or destination wiring.

Syntax

**C#**



public enum SymbolReference.PointVariant : System.Enum

public enum class SymbolReference.PointVariant : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **NOT\_RELVANT** | 0 | Instance has no different wiring type styles |
| **NOT\_SPECIFIC** | 1 | Instance uses own wiring type (use only for settings) |
| **POINT\_WIRING** | 2 | Instance uses point wiring variant for graphical appearance |
| **TARGET\_WIRING** | 3 | Instance uses normal variant for graphical appearance |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.DataModel.SymbolReference.PointVariant**
