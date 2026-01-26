# IMessage.Classification

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage+Classification.html

---

Pre- defined classifications for project messages; every project message must be assigned to one of these classifications, other values will not be supported. The classification of a project message could be changed in the settings dialog at run time.

Syntax

**C#**



public enum IMessage.Classification : System.Enum

public enum class IMessage.Classification : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Error** | 2 |  |
| **Hint** | 0 |  |
| **Unknown** | -1 |  |
| **Warning** | 1 |  |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.EServices.IMessage.Classification**
