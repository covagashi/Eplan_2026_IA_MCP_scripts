# GetSearchDBEntries Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~GetSearchDBEntries.html

---

Returns objects from a list of search results.

Syntax

**C#**



public StorableObject[] GetSearchDBEntries( 

   Project pProject,

   uint nStartIndex,

   uint nCount

)

public:

array<StorableObject^>^ GetSearchDBEntries( 

   Project^ pProject,

   uint nStartIndex,

   uint nCount

)


#### Parameters

*pProject*
:   Project of which the results list entries will be returned.

*nStartIndex*
:   Start list index of the objects to return. 0 means objects starting with the first list position are returned.

*nCount*
:   Maximum count of objects to return.

#### Return Value

Found objects.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the project is not valid. |
| **ApplicationException** | \Internal interface for search could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The method finished with errors. |
