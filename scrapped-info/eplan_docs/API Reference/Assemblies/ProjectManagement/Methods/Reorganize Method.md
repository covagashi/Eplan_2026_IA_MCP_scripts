# Reorganize Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~Reorganize.html

---

Reorganizes a project

Syntax

**C#**



public void Reorganize( 

   Project oProject,

   bool bExtendedReoganize

)

public:

void Reorganize( 

   Project^ oProject,

   bool bExtendedReoganize

)


#### Parameters

*oProject*
:   Project which will be reorganized.

*bExtendedReoganize*
:   Extended reoganize option

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing arguments. |
| **ArgumentException** | Thrown in case if invalid arguments, e.g. an invalid project is set. |
| **ApplicationException** | Thrown, if the \internal action could no be found. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while executing the method. |
