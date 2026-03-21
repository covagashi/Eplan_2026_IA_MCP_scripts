# Renumber.Enums.Parts

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Renumber+Enums+Parts.html

---

Parameter enum for parts list position numbering. The enum determines, which kinds of parts will be numbered. The enum \members may be combined by a logical or (|), e.g.: DeviceTagsWithoutPartNumber | ClampParts

Syntax

**C#**



public enum Renumber.Enums.Parts : System.Enum

public enum class Renumber.Enums.Parts : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **BusBarConnectorParts** | 64 | Include busbar connector parts. |
| **CableParts** | 4 | Include cable parts. |
| **CableProjectParts** | 16 | Include cable project parts. |
| **ClampParts** | 2 | Include terminal parts. |
| **ConnectionParts** | 8 | Include wire parts. |
| **DeviceTagsWithoutPartNumber** | 1 | Consider also devices without parts. |
| **PinAndJackParts** | 32 | Include pin and jack parts. |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.HEServices.Renumber.Enums.Parts**
