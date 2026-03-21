# CreateTransaction Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.TransactionManager~CreateTransaction.html

---

Creates object representing a read-write transaction.

Syntax

**C#**



public Transaction CreateTransaction()

public:

Transaction^ CreateTransaction();


#### Return Value

[Transaction](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Transaction.html) object.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when a Transaction object has already been obtained and not disposed. |
| [DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when a read-write transaction is being opened while read-only transaction is running. |
