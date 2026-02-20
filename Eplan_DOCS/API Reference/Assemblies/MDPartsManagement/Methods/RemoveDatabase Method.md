# RemoveDatabase Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~RemoveDatabase.html

---

Removes the given parts database.

Syntax

**C#**



public void RemoveDatabase( 

   string databaseName

)

public:

void RemoveDatabase( 

   String^ databaseName

)


#### Parameters

*databaseName*
:   The file name of Eplan database or a string for selecting a SQL Server database. The syntax of that string is: "Server|Database|0" Windows authentication "Server|Database|2|Username|Password" SQL Server authentication, username and password not encrypted.

Exceptions

| Exception | Description |
| --- | --- |
| [MDArgumentNullException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDArgumentNullException.html) | Thrown when database name is null |
| [MDInvalidArgumentException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDInvalidArgumentException.html) | Thrown when database name is empty |
