# SetSQLServerConnectionParameters Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~SetSQLServerConnectionParameters.html

---

Sets SQL connection parameters.

Syntax

**C#**



public void SetSQLServerConnectionParameters( 

   string strServer,

   string strDatabase,

   ProjectManagement.AuthenticationType eAuthType,

   string strUser,

   string strPassword,

   bool bRememberPass

)

public:

void SetSQLServerConnectionParameters( 

   String^ strServer,

   String^ strDatabase,

   ProjectManagement.AuthenticationType eAuthType,

   String^ strUser,

   String^ strPassword,

   bool bRememberPass

)


#### Parameters

*strServer*
:   Server path

*strDatabase*
:   Database name

*eAuthType*
:   Authentication type: Windows authentication or SQL server

*strUser*
:   Database user name - used only when authentication type is SQL server.

*strPassword*
:   Database user's password - used only when authentication type is SQL server.

*bRememberPass*
:   Password remember.

Remarks

Changes will be done if current database type is set to SQL. Please take into account that calling the method changes ProjectManagement.ProjectManagementDatabase property also.
