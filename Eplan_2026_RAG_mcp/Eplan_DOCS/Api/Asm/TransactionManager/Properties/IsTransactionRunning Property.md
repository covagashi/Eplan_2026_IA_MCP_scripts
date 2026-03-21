# IsTransactionRunning Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.TransactionManager~IsTransactionRunning.html

---

Tells if a read-write API transaction is open.

Syntax

**C#**



public bool IsTransactionRunning {get;}

public:

property bool IsTransactionRunning {

   bool get();

}


#### Property Value

true, when there is an open read-write transaction false, when a read-write transaction is not open

Remarks

API transaction is a transactions which was explicitly or implicitly started from API.
