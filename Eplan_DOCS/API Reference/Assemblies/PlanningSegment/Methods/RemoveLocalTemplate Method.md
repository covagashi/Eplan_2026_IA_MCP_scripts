# RemoveLocalTemplate Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~RemoveLocalTemplate.html

---

Removes a local template from this object.

Syntax

**C#**



public void RemoveLocalTemplate( 

   StorableObject pLocalTemplate

)

public:

void RemoveLocalTemplate( 

   StorableObject^ pLocalTemplate

)


#### Parameters

*pLocalTemplate*
:   Template object to be removed.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if parameter is `null`. |
| [System.InvalidOperationException](#) | Thrown if template is invalid or does not belong to this object. |

Remarks

If [SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~SegmentTemplate.html) is assigned then local template are taken from specification and can't be changed.
