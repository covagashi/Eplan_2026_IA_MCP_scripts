# ConnectionService.DesignateOverwrition

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService+DesignateOverwrition.html

---

Mode for overwriting connection designations.

Syntax

**C#**



public enum ConnectionService.DesignateOverwrition : System.Enum

public enum class ConnectionService.DesignateOverwrition : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **All** | 0 | always overwrite |
| **ExceptManuals** | 1 | overwrite all except those, which are marked as 'manually set' |
| **None** | 2 | never overwrite |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.HEServices.ConnectionService.DesignateOverwrition**
