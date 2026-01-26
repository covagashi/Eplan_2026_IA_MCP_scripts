# ImportDescriptions Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PrePlanningService~ImportDescriptions.html

---

Imports descriptions from pre-planning to project.

Syntax

**C#**



public bool ImportDescriptions( 

   Project pProject

)

public:

bool ImportDescriptions( 

   Project^ pProject

)


#### Parameters

*pProject*
:   Project to which pre-planning descriptions are imported. Can't be `null`.

#### Return Value

Returns `true` if import is successful.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter `pProject` is a `null` value. |
