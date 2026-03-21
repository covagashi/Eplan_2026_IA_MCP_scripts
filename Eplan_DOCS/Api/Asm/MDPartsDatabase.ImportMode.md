# MDPartsDatabase.ImportMode

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase+ImportMode.html

---

Import mode

Syntax

**C#**



public enum MDPartsDatabase.ImportMode : System.Enum

public enum class MDPartsDatabase.ImportMode : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **AppendNewRecords** | 0 | append new records only |
| **ReplaceAndAppend** | 3 | replace existing records and append new ones |
| **UpdateAndAppend** | 2 | update existing records and append new ones |
| **UpdateExistingRecords** | 1 | update existing records only |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.MasterData.MDPartsDatabase.ImportMode**
