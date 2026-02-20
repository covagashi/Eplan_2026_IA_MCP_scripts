# ReorganizeStructure Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PrePlanningService~ReorganizeStructure.html

---

Reorganizes structure of planning objects in given project.

Syntax

**C#**



public bool ReorganizeStructure( 

   Project pProject

)

public:

bool ReorganizeStructure( 

   Project^ pProject

)


#### Parameters

*pProject*
:   Project which planning structure will be reorganizated. Can't be `null`.

#### Return Value

Returns `false`, if locking of required objects was not possible.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Null was set to a parameter. |

Remarks

This method reorganizes structure (looks for planning objects with bit-flag "HAS\_CHANGES4SUBOBJECTS") of planning objects in given project. It also updates article references of children and re-numerates functions according to changed project structures.
