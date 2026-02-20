# DeleteStoredProperties(Project,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PartsService~DeleteStoredProperties(Project,String).html

---

Deletes stored properties from a project.

Syntax

**C#**



public void DeleteStoredProperties( 

   Project oProject,

   string strConfigScheme

)

public:

void DeleteStoredProperties( 

   Project^ oProject,

   String^ strConfigScheme

)


#### Parameters

*oProject*
:   Project from which stored properties will be deleted.

*strConfigScheme*
:   Configuration scheme. If an empty string is passed to the parameter method will use scheme which is currently set in GUI.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing arguments. |
| **ArgumentException** | Thrown in case if invalid arguments, e.g. an invalid project is set. |
| **ApplicationException** | Internal interface for deleting stored properties could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during deleting stored properties. |
