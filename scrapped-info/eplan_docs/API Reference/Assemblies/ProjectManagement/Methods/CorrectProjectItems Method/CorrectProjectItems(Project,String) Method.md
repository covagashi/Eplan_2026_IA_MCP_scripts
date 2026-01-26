# CorrectProjectItems(Project,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~CorrectProjectItems(Project,String).html

---

Corrects project items.

Syntax

**C#**



public void CorrectProjectItems( 

   Project oProject,

   string strScheme

)

public:

void CorrectProjectItems( 

   Project^ oProject,

   String^ strScheme

)


#### Parameters

*oProject*
:   Project which items will be corrected.

*strScheme*
:   Scheme name.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing arguments. |
| **ArgumentException** | Thrown in case if invalid arguments, e.g. an invalid project is set. |
| **ApplicationException** | Thrown, if the \internal action could no be found. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while executing the method. |
