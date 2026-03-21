# SelectProjectInPagesNavigator Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~SelectProjectInPagesNavigator.html

---

Selects the project in pages navigator

Syntax

**C#**



public bool SelectProjectInPagesNavigator( 

   Project oProject

)

public:

bool SelectProjectInPagesNavigator( 

   Project^ oProject

)


#### Parameters

*oProject*
:   project to select

#### Return Value

TRUE if operation succeeded and FALSE if not.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Invalid parameters found. |
| [System.ArgumentNullException](#) | Null was passed to a parameter. |
| [System.ApplicationException](#) | The internal interface could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred. Please refer to the exception message. |
