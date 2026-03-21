# UpdateScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~UpdateScheme.html

---

Updates the scheme of the database.

Syntax

**C#**



public void UpdateScheme()

public:

void UpdateScheme();


Remarks

If the scheme is already up to date, than nothing will be done. OpenDatabase method does not automatically update a parts database from a previous to the current version. Databases in an older format will be opened read-only. You can check whether the database format is up-to-date by the property MDPartsDatabase.IsSchemeUpToDate and update it if needed by this method. Parts databases prior to version 2022 need to be upgraded / converted either manually or by the action XPamConvertPartDatabaseToArticleDatabaseAction /OldDatabase... /NewDatabase...

Example

**C#**

```
MDPartsDatabase database = partsManagement.OpenDatabase();

if ( !database.IsSchemeUpToDate )

{

 database.UpdateScheme();

}
```
