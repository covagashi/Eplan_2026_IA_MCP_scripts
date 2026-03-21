# GetAllSearchDBEntries Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~GetAllSearchDBEntries.html

---

\Returns all objects in a list of search results.

Syntax

**C#**



public StorableObject[] GetAllSearchDBEntries( 

   Project pProject

)

public:

array<StorableObject^>^ GetAllSearchDBEntries( 

   Project^ pProject

)


#### Parameters

*pProject*
:   Project of which the results list entries will be returned.

#### Return Value

All found objects.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the project is not valid. |
| **ApplicationException** | \Internal interface for search could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The method finished with errors. |
