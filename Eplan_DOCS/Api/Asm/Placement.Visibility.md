# Placement.Visibility

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement+Visibility.html

---

Possible visibility states. These values are return by the [Placement.IsSetAsVisible](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsSetAsVisible.html) property.

Syntax

**C#**



public enum Placement.Visibility : System.Enum

public enum class Placement.Visibility : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **ByLayer** | 2 | Visibility of the placement object is determined by the setting of the layer that it is placed on. |
| **Invisible** | 1 | The placement object is set to be invisible |
| **Visible** | 0 | The placement object is set to be visible. |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.DataModel.Placement.Visibility**
