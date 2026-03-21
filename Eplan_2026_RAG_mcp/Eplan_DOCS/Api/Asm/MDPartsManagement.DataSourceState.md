# MDPartsManagement.DataSourceState

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement+DataSourceState.html

---

State of connection to database that is currently used.

Syntax

**C#**



public enum MDPartsManagement.DataSourceState : System.Enum

public enum class MDPartsManagement.DataSourceState : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **API** | 2 | Api action is used |
| **Connected2eStock** | 3 | Connected to eStock |
| **Default** | 0 | Connected to default database |
| **NotConnected** | 5 | Not connected to any database |
| **ReadOnly** | 4 | Connected readonly |
| **SQL\_Server** | 1 | Connected to SQL Server |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.MasterData.MDPartsManagement.DataSourceState**
