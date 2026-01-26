# Abort Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Transaction~Abort.html

---

Aborts the transaction. Cannot be called more than one time for given transaction.

Syntax

**C#**



public void Abort()

public:

void Abort();


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when Transaction has already been committed or aborted. |
