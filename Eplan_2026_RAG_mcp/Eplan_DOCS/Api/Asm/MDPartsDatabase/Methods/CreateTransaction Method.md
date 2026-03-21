# CreateTransaction Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~CreateTransaction.html

---

Creates a new database transaction.

Syntax

**C#**



public MDPartsDatabaseTransaction CreateTransaction()

public:

MDPartsDatabaseTransaction^ CreateTransaction();


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
