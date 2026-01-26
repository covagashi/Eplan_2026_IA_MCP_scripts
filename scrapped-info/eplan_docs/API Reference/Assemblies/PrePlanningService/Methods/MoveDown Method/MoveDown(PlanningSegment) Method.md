# MoveDown(PlanningSegment) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PrePlanningService~MoveDown(PlanningSegment).html

---

Moves object one position down in navigator.

Syntax

**C#**



public void MoveDown( 

   PlanningSegment plaObject

)

public:

void MoveDown( 

   PlanningSegment^ plaObject

)


#### Parameters

*plaObject*
:   Object which should be moved. Can't be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter `plaObject` is a `null` value. |
| [System.ArgumentException](#) | Thrown when `plaObject` have `null` parent. |

Remarks

Moving object is related to its parent so items without parent won't be moved. When given object is last or only child also no action will be performed as there is nothing to do.
