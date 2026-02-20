# CompressProject(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~CompressProject(String,String).html

---

Compresses a project.

Syntax

**C#**



public void CompressProject( 

   string strFullLinkFileName,

   string strConfigScheme

)

public:

void CompressProject( 

   String^ strFullLinkFileName,

   String^ strConfigScheme

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project to be compressed.

*strConfigScheme*
:   Configuration scheme. If an empty string is passed to the parameter, the last\-used scheme will be reused which is currently set in GUI.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing arguments. |
| **ArgumentException** | Thrown in case if invalid arguments, e.g. an invalid project is set. |
| **ApplicationException** | \Internal interface for compressing could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred when compressing the project. |

Remarks

The specified project may be open or not. If the project was not open already, it will be opened for compressing and will be closed subsequently.
