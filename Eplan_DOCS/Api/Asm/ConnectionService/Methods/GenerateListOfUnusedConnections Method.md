# GenerateListOfUnusedConnections Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService~GenerateListOfUnusedConnections.html

---

Generates list of unused or deleted connection from project.

Syntax

**C#**



public bool GenerateListOfUnusedConnections( 

   Project oPrj,

   string strFileNameFullPath,

   bool bExportOnlyDeletedConnections

)

public:

bool GenerateListOfUnusedConnections( 

   Project^ oPrj,

   String^ strFileNameFullPath,

   bool bExportOnlyDeletedConnections

)


#### Parameters

*oPrj*
:   Project from which generation of list will be done.

*strFileNameFullPath*
:   Full path to file into which list will be writen.

*bExportOnlyDeletedConnections*
:   If true only deleted connection will be added to list.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ArgumentNullException](#) | Thrown when neccessary argument is `null`. |
| [System.ApplicationException](#) | The internal interface used for export could not be created. |
| [System.UnauthorizedAccessException](#) | No user rights to create files on the file system. |
