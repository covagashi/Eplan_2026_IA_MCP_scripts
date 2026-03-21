# WindowMacro.Enums.NumerationMode

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro+Enums+NumerationMode.html

---

This enumeration specifies insertion mode, when inserting a macro via the Eplan.EplApi.HeServices.Insert class

Syntax

**C#**



public enum WindowMacro.Enums.NumerationMode : System.Enum

public enum class WindowMacro.Enums.NumerationMode : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **None** | 1 | Corresponds with 'Do not modify'. Designation properties of the device tag is changed according to the page (default). In 3D works as Ignore. |
| **Number** | 2 | Corresponds to 'Number'. |
| **NumberPreferPrefix** | 4 | Corresponds to 'Number' with the flag 'Number prefix if existing" set. |
| **NumberWithQuestionMark** | 3 | Corresponds to 'Number with flag '?''. |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.DataModel.MasterData.WindowMacro.Enums.NumerationMode**
