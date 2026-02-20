# CorrectProjectItems(Function[],String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~CorrectProjectItems(Function[],String).html

---

Corrects project items.

Syntax

**C#**



public void CorrectProjectItems( 

   Function[] arrFunctions,

   string strScheme

)

public:

void CorrectProjectItems( 

   array<Function^>^ arrFunctions,

   String^ strScheme

)


#### Parameters

*arrFunctions*
:   Array of functions which will be corrected.

*strScheme*
:   Scheme name.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing arguments. |
| **ArgumentException** | Thrown in case if invalid arguments, e.g. array do not contain any valid objects. |
| **ApplicationException** | Thrown, if the \internal action could no be found. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while executing the method. |

Remarks

Connections in project will be also corrected if such option is selected in scheme.
