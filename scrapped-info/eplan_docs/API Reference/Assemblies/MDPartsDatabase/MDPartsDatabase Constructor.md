# MDPartsDatabase Constructor

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~_ctor(String).html

---

Opens parts database

Syntax

**C#**



public MDPartsDatabase( 

   string databaseName

)

public:

MDPartsDatabase( 

   String^ databaseName

)


#### Parameters

*databaseName*
:   The file name of EPLAN database. or a string for selecting a SQL Server database. The syntax of that string is: "Server|Database|0" Windows authentication "Server|Database|2|Username|Password" SQL Server authentication, username and password not encrypted.

Remarks

This or MDPartsManagement.OpenDatabase method does not automatically update a parts database from a previous to the current version. Databases in an older format will be opened read-only. You can check whether the database format is up-to-date by the property MDPartsDatabase.IsSchemeUpToDate and update it if needed by the method MDPartsDatabase.UpdateScheme(). Parts databases prior to version 2022 need to be upgraded / converted either manually or by the action XPamConvertPartDatabaseToArticleDatabaseAction /OldDatabase... /NewDatabase...
