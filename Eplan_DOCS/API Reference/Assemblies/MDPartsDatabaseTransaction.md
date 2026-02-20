# MDPartsDatabaseTransaction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseTransaction.html

---

A transaction object for a parts database

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.MasterData.MDPartsDatabaseTransaction**

Syntax

**C#**



public class MDPartsDatabaseTransaction

public ref class MDPartsDatabaseTransaction


Remarks

working on parts database items can be done using transactions. When using transactions all changed items will be stored when calling transction.Commit(); using transctions is optional. If no transaction is used the changes will be written to the database on every changing of an MDPartsDatabaseItem object. When a MDPartsDatabaseItem will be changed on a lot of properties it's recommended to use transactions.

Example

**C#**

```
MDPartsDatabaseTransaction dbTransaction = database.CreateTransaction();

MDPart part = database.GetPart("myPart");

if (part != null)

{

 part.PartNr = "myNewPart";

 dbTransaction.Commit();

}
```

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Commit](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseTransaction~Commit.html) | Commit the database transaction. All changed MDPartsDatabaseItem objects will be stored in the database. |
| Public Method | [Dispose](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseTransaction~Dispose().html) | Destructor for deterministic finalization of MDPartsDatabaseTransaction object. |
| Public Method | [Rollback](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseTransaction~Rollback.html) | Rollback the database transaction. The changes are not stored. |


