# ClearSearchDB Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~ClearSearchDB.html

---

Clears the list of search results.

Syntax

**C#**



public void ClearSearchDB( 

   Project pProject

)

public:

void ClearSearchDB( 

   Project^ pProject

)


#### Parameters

*pProject*
:   Project of which the list of search results will be cleared.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the project is not valid. |
| **ApplicationException** | \Internal interface for search could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The method finished with errors. |
