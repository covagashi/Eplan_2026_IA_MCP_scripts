# Connections(String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Generate~Connections(String,Boolean).html

---

Updates connections in the given project.

Syntax

**C#**



public void Connections( 

   string strFullLinkFileName,

   bool bRebuildAllConnections

)

public:

void Connections( 

   String^ strFullLinkFileName,

   bool bRebuildAllConnections

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project in which to update all connections.

*bRebuildAllConnections*
:   If true rebuilds all connections else updates only.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid project. |
| **ApplicationException** | The internal interface for generating connections could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during connection generation. Please refer to the exception message. |
