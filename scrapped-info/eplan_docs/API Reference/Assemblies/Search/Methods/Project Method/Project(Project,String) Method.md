# Project(Project,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~Project(Project,String).html

---

Searches on the specified project for a search string. The search settings will influence the result. The found object will be written to the active list of results.

Syntax

**C#**



public void Project( 

   Project pProject,

   string searchString

)

public:

void Project( 

   Project^ pProject,

   String^ searchString

)


#### Parameters

*pProject*
:   Project for which the search is conducted.

*searchString*
:   Text to search for.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the project is not valid. |
| **ApplicationException** | \Internal interface for search could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The search finished with errors. |
