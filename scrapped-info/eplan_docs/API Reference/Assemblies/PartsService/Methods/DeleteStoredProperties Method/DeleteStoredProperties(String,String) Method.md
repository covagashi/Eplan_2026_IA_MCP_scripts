# DeleteStoredProperties(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PartsService~DeleteStoredProperties(String,String).html

---

Deletes stored properties from a project.

Syntax

**C#**



public void DeleteStoredProperties( 

   string strFullLinkFileName,

   string strConfigScheme

)

public:

void DeleteStoredProperties( 

   String^ strFullLinkFileName,

   String^ strConfigScheme

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project from which properties should be deleted.

*strConfigScheme*
:   Configuration scheme. If an empty string is passed to the parameter method will use scheme which is currently set in GUI.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing arguments. |
| **ArgumentException** | Thrown in case if invalid arguments, e.g. an invalid project is set. |
| **ApplicationException** | Internal interface for deleting stored properties could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during deleting stored properties. |

Remarks

The specified project may be open or not. If the project was not open, it will be opened for deleting stored properties and will be closed subsequently.
