# CompleteProject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata~CompleteProject.html

---

Method for completing project master data.

Syntax

**C#**



public void CompleteProject( 

   Project oProject

)

public:

void CompleteProject( 

   Project^ oProject

)


#### Parameters

*oProject*
:   Project to be completed.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | A parameter was set to a null reference. |
| **ArgumentException** | \Parameters are invalid, e.g. the project does not exist or is invalid. |
| **ApplicationException** | \Internal interface for master data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Project could not be completed. |
