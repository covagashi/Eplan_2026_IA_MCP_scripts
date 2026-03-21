# ConnectionService.Deletion

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService+Deletion.html

---

Mode for deleting wire designations and connection definition points

Syntax

**C#**



public enum ConnectionService.Deletion : System.Enum

public enum class ConnectionService.Deletion : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **ConnectionDefinitionPoints** | 1 | delete only those connection definition points that have unspecified designations (i.e. those that have CONNECTION\_DESIGNATION property empty) |
| **Designations** | 0 | delete only designations |
| **DesignationsAndCDPs** | 2 | delete designation and connection definition points |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.HEServices.ConnectionService.Deletion**
