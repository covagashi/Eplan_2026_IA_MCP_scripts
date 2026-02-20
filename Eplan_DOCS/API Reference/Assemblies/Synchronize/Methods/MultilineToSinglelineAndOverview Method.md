# MultilineToSinglelineAndOverview Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~MultilineToSinglelineAndOverview.html

---

Synchronization from 'multi-line' data onto 'single-line' and 'overview' data.

Syntax

**C#**



public void MultilineToSinglelineAndOverview( 

   Project oProject

)

public:

void MultilineToSinglelineAndOverview( 

   Project^ oProject

)


#### Parameters

*oProject*
:   Project that will be synchronized.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the project is not valid. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The synchronization finished with errors. |
