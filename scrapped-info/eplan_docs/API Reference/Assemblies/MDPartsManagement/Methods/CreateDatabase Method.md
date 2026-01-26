# CreateDatabase Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~CreateDatabase.html

---

Create a new parts database.

Syntax

**C#**



public MDPartsDatabase CreateDatabase( 

   string databaseName

)

public:

MDPartsDatabase^ CreateDatabase( 

   String^ databaseName

)


#### Parameters

*databaseName*
:   The file name of Eplan database or a string for selecting a SQL Server database. The syntax of that string is: "Server|Database|0" Windows authentication "Server|Database|2|Username|Password" SQL Server authentication, username and password not encrypted.

Exceptions

| Exception | Description |
| --- | --- |
| [MDDatabaseReadOnlyException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDDatabaseReadOnlyException.html) | If database is read only or the scheme is not up to date |
