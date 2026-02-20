# IsImplicitEplanTransactionCommited Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Transaction~IsImplicitEplanTransactionCommited.html

---

Transaction property which returns true if an implicit Eplan transaction was started and finished during lifetime of current transaction.

Syntax

**C#**



public bool IsImplicitEplanTransactionCommited {get;}

public:

property bool IsImplicitEplanTransactionCommited {

   bool get();

}


#### Property Value

true, when there was an internal commit false, when no internal commit was performed
