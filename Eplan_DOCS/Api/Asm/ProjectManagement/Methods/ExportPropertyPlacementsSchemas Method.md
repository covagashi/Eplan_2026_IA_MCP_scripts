# ExportPropertyPlacementsSchemas Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~ExportPropertyPlacementsSchemas.html

---

Exports property placements schemes.

Syntax

**C#**



public void ExportPropertyPlacementsSchemas( 

   Project oProject,

   string strFileName

)

public:

void ExportPropertyPlacementsSchemas( 

   Project^ oProject,

   String^ strFileName

)


#### Parameters

*oProject*
:   Project from which property placements schemes will be exported.

*strFileName*
:   Full name of output file.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing arguments. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. an invalid project is set. |
| **ApplicationException** | Thrown if the \internal action could no be found. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while executing the method. |
