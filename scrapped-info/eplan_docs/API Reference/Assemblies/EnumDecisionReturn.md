# EnumDecisionReturn

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.EnumDecisionReturn.html

---

This enum is returned by the [Decider](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Decider.html) method.

Syntax

**C#**



public enum EnumDecisionReturn : System.Enum

public enum class EnumDecisionReturn : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **eABORT** | 3 | Abort was pressed |
| **eCANCEL** | 2 | Cancel was pressed |
| **eCLOSE** | 8 | Close was pressed |
| **eERROR\_WHILEOPENINGDECIDER** | -2 | return code for errors while opening the decider dialog |
| **eIGNORE** | 5 | Ignore was pressed |
| **eNO** | 7 | No was pressed |
| **eNO\_ALL** | 1001 | NoAll was pressed |
| **eOK** | 1 | Ok was pressed |
| **eRETRY** | 4 | Retry was pressed |
| **eSYSERROR\_NOTQUIET** | -1 | code for display of errors. dialog will appear in batch or quit mode |
| **eUNDEFINED** | 0 | invalid value was returned |
| **eYES** | 6 | Yes was pressed |
| **eYES\_ALL** | 1000 | YesAll was pressed |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.Base.EnumDecisionReturn**
