# AddToSearchDB(StorableObject[]) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~AddToSearchDB(StorableObject[]).html

---

Adds objects to the currently active list of search results.

Syntax

**C#**



public void AddToSearchDB( 

   StorableObject[] storableObjects

)

public:

void AddToSearchDB( 

   array<StorableObject^>^ storableObjects

)


#### Parameters

*storableObjects*
:   Objects to add.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments (storableObject is not valid). |
| **ApplicationException** | \Internal interface for search could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The method finished with errors. |
