# Renumber.Enums.DeviceTags

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Renumber+Enums+DeviceTags.html

---

Parameter enum for device tag numbering. The enum members can be combined by a logical or (|), e.g. OmitNumeratedBySPS | NumerateCables.

Syntax

**C#**



public enum Renumber.Enums.DeviceTags : System.Enum

public enum class Renumber.Enums.DeviceTags : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **NumerateCables** | 4 | Also renumber cables, if their device tags contain source and target information. |
| **OmitNumeratedBySPS** | 2 | Don't change device tags, which are influenced by PLC numbering. |
| **PostNumerate** | 1 | If this flag is set, only invalid device tags (i.e. those containing '?' character) will be renumbered |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.HEServices.Renumber.Enums.DeviceTags**
