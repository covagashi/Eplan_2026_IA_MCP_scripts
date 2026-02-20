# IsReadOnly Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~IsReadOnly.html

---

Returns true if the parts database is read only. That can be if the EPLAN database file has read only attribute set, or the SQL Server has write restrictions to the current user.

Syntax

**C#**



public bool IsReadOnly {get;}

public:

property bool IsReadOnly {

   bool get();

}


Remarks

OpenDatabase method does not automatically update a parts database from a previous to the current version. Databases in an older format will be opened read-only. You can check whether the database format is up-to-date by the property MDPartsDatabase.IsSchemeUpToDate and update it if needed by the method MDPartsDatabase.UpdateScheme(). Parts databases prior to version 2022 need to be upgraded / converted either manually or by the action XPamConvertPartDatabaseToArticleDatabaseAction /OldDatabase... /NewDatabase...
