# IsSchemeUpToDate Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~IsSchemeUpToDate.html

---

Test, whether the scheme of the database is up to date.

Syntax

**C#**



public bool IsSchemeUpToDate {get;}

public:

property bool IsSchemeUpToDate {

   bool get();

}


Remarks

Returns true, if the scheme if up to date, otherwise false. OpenDatabase method does not automatically update a parts database from a previous to the current version. Databases in an older format will be opened read-only. You can check whether the database format is up-to-date by this property and update it if needed by the method MDPartsDatabase.UpdateScheme(). Parts databases prior to version 2022 need to be upgraded / converted either manually or by the action XPamConvertPartDatabaseToArticleDatabaseAction /OldDatabase... /NewDatabase...
