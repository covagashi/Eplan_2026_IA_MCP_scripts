# OverviewToMultilineAndSingleline Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~OverviewToMultilineAndSingleline.html

---

Synchronization from 'overview' data onto 'single-line' and 'multi-line' data.

Syntax

**C#**



public void OverviewToMultilineAndSingleline( 

   Project oProject

)

public:

void OverviewToMultilineAndSingleline( 

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
