# CompressProject(Project,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~CompressProject(Project,String).html

---

Compresses a project.

Syntax

**C#**



public void CompressProject( 

   Project oProject,

   string strConfigScheme

)

public:

void CompressProject( 

   Project^ oProject,

   String^ strConfigScheme

)


#### Parameters

*oProject*
:   Project to be compressed.

*strConfigScheme*
:   Configuration scheme. If an empty string is passed to the parameter, the last\-used scheme will be reused which is currently set in GUI.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing arguments. |
| **ArgumentException** | Thrown in case if invalid arguments, e.g. an invalid project is set. |
| **ApplicationException** | \Internal interface for compressing could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred when compressing the project. |
| **InvalidScheme** | An error occurrs when used scheme name doesn't exist |
