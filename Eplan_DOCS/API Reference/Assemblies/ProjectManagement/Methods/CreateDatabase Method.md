# CreateDatabase Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~CreateDatabase.html

---

Create a new projectmanagement database.

Syntax

**C#**



public void CreateDatabase( 

   string strDatabase

)

public:

void CreateDatabase( 

   String^ strDatabase

)


#### Parameters

*strDatabase*
:   The file name of EPLAN database or a string for selecting a SQL Server database. The syntax of that string is: "Server|Database|0" Windows authentication "Server|Database|2|Username|Password" SQL Server authentication, username and password not encrypted.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown when empty string was passed as an argument. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of problems with database creation. |

Remarks

Beware: when database with given name already exists it will be overwritten.
