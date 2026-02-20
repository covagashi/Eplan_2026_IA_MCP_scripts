# UpdateDetailPlanning(PlanningSegment) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PrePlanningService~UpdateDetailPlanning(PlanningSegment).html

---

Updates data to ensure that the property values in planning object are the same as in assigned functions.

Syntax

**C#**



public void UpdateDetailPlanning( 

   PlanningSegment pPlanningSegment

)

public:

void UpdateDetailPlanning( 

   PlanningSegment^ pPlanningSegment

)


#### Parameters

*pPlanningSegment*
:   Planning segment will be used. Can't be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter `pPlanningSegment` is a `null` value. |

Remarks

If a placeholder is use in macro to transfer properties from planning object to the functions of the macro, the values from planning object are copied while placing the macro. If the planning object is changed afterwards, the values at the functions stay the same and are different now. This method copies this properties again, so that the property values in planning object are the same as in assigned functions.
