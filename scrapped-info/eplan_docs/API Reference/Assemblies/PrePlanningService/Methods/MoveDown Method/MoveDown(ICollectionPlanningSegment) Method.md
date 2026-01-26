# MoveDown(ICollection<PlanningSegment>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PrePlanningService~MoveDown(ICollection{PlanningSegment}).html

---

Moves objects one position down in navigator.

Syntax

**C#**



public void MoveDown( 

   ICollection<PlanningSegment> colObjects

)

public:

void MoveDown( 

   ICollection<PlanningSegment^>^ colObjects

)


#### Parameters

*colObjects*
:   Collection of pre planning objects which should be moved. Can't be `null` or empty.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter `colObjects` is a `null` value. |
| [System.ArgumentException](#) | Thrown when collection `colObjects` is empty or when any of objects have different parent. |

Remarks

All objects in collection needs to have the same parent. In other case none of them will be moved. Parent of first object is considered as correct parent. If any of objects is last child it won't be moved. There is no matter in what order items in collection will be passed.
