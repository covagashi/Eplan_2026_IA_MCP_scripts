# Transaction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Transaction.html

---

Class representing DataModel's transaction. It implements [System.IDisposable](#) interface. Must be disposed immediately after transaction's end.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.ITransaction](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ITransaction.html)  
      **Eplan.EplApi.DataModel.Transaction**

Syntax

**C#**



public sealed class Transaction : ITransaction

public ref class Transaction sealed : public ITransaction


Remarks

For details, please refer to [Transactions](Transactions.html) chapter of API Help.

Example

Transaction usage - only inside "using".

- [c#](#i-tab-content-7f14fd95-f55f-412f-8871-cd056f9b7f6e)

```
using (Transaction txn = new TransactionManager().CreateTransaction())

{

    Function f;

    f.Name = "F1";

    txn.Commit();

}
```

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [IsImplicitEplanTransactionCommited](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Transaction~IsImplicitEplanTransactionCommited.html) | Transaction property which returns true if an implicit Eplan transaction was started and finished during lifetime of current transaction. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Abort](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Transaction~Abort.html) | Aborts the transaction. Cannot be called more than one time for given transaction. |
| Public Method | [Commit](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Transaction~Commit.html) | Overridden. Commits the transaction. Cannot be called more than one time for given transaction. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ITransaction~Dispose().html) | Destructor for deterministic finalization of Transaction object. (Inherited from [Eplan.EplApi.DataModel.ITransaction](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ITransaction.html)) |
| Public Method | [Store](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Transaction~Store.html) | This method will enable to commit the transaction, and \internal open the next transaction. |


