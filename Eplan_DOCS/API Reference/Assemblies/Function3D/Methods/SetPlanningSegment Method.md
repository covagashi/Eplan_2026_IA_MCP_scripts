# SetPlanningSegment Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~SetPlanningSegment.html

---

Assigns [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) to this function3d.

Syntax

**C#**



public void SetPlanningSegment( 

   PlanningSegment pPlanningSegment

)

public:

void SetPlanningSegment( 

   PlanningSegment^ pPlanningSegment

)


#### Parameters

*pPlanningSegment*
:   [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) which will be assigned to function3d, or `null` to remove planning object from function3d.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) | Thrown when parent object for [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) is [CopperBundle](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.CopperBundle.html), [BusBarSystem](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBarSystem.html) or [Drilling](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling.html). |
| [System.NotImplementedException](#) | Thrown when implementation of requested interface isn't found. |

Remarks

Setting [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) is forbidden for [CopperBundle](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.CopperBundle.html), [BusBarSystem](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBarSystem.html) and [Drilling](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling.html) as this objects are not written in macros.
