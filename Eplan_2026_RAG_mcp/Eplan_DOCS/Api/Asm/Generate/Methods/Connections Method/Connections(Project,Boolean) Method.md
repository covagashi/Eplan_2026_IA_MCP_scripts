# Connections(Project,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Generate~Connections(Project,Boolean).html

---

Updates connections in the given project.

Syntax

**C#**



public void Connections( 

   Project oProject,

   bool bRebuildAllConnections

)

public:

void Connections( 

   Project^ oProject,

   bool bRebuildAllConnections

)


#### Parameters

*oProject*
:   Project in which to update all connections.

*bRebuildAllConnections*
:   If true rebuilds all connections else updates only.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid project. |
| **ApplicationException** | The internal interface for generating connections could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during connection generation. Please refer to the exception message. |
