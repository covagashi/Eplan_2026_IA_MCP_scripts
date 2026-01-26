# AddRelatedObjectsToGotoDB Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~AddRelatedObjectsToGotoDB.html

---

Adds cross-referenced objects to the goto results list.

Syntax

**C#**



public void AddRelatedObjectsToGotoDB( 

   StorableObject storableObject

)

public:

void AddRelatedObjectsToGotoDB( 

   StorableObject^ storableObject

)


#### Parameters

*storableObject*
:   Object of which the cross\-references should be found.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments (storableObject is not valid). |
| **ApplicationException** | \Internal interface for search could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The method finished with errors. |
