# HarnessService.FilterMode

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.HarnessService+FilterMode.html

---

Scope of data export

Syntax

**C#**



public enum HarnessService.FilterMode : System.Enum

public enum class HarnessService.FilterMode : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **HarnessAll** | 1 | Export all functions, connections and harness objects in project without any filtering |
| **HarnessRelated** | 0 | Export all harness objects together with directly assigned and indirectly related objects, |
| **HarnessSelection** | 2 | If functions or connections assigned to harness in selection, apply mode "HarnessRelated", otherwise "HarnessAll" |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.HEServices.HarnessService.FilterMode**
