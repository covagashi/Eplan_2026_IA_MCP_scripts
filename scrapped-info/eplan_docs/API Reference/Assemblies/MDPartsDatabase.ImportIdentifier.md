# MDPartsDatabase.ImportIdentifier

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase+ImportIdentifier.html

---

Import Identifier

Syntax

**C#**



public enum MDPartsDatabase.ImportIdentifier : System.Enum

public enum class MDPartsDatabase.ImportIdentifier : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **PartNumber** | 0 | Find the same parts with the partnumber |
| **UniqueId** | 1 | Find the same parts with the unique id |
| **UniqueIdOptPartNumber** | 2 | Find the same parts with the unique id and the partnumber, if unique id is missing. |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.MasterData.MDPartsDatabase.ImportIdentifier**
