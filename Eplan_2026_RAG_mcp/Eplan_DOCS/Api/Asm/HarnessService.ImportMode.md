# HarnessService.ImportMode

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.HarnessService+ImportMode.html

---

Mode for the import can be a combination of following values

Syntax

**C#**



[Flags()]

public enum HarnessService.ImportMode : System.Enum

[Flags()]

public enum class HarnessService.ImportMode : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Change** | 2 | Change only existing objects |
| **Create** | 1 | Create only missing objects |
| **Delete** | 4 | Delete only unnecessary existing objects |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.HEServices.HarnessService.ImportMode**
