# Connections(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Generate~Connections(String).html

---

Updates connections in the given project.

Syntax

**C#**



public void Connections( 

   string strFullLinkFileName

)

public:

void Connections( 

   String^ strFullLinkFileName

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project in which to update all connections.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid project. |
| **ApplicationException** | The internal interface for generating connections could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during connection generation. Please refer to the exception message. |
