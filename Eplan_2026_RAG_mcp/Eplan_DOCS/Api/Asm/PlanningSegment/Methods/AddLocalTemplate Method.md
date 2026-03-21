# AddLocalTemplate Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~AddLocalTemplate.html

---

Add new local template based on function definition.

Syntax

**C#**



public StorableObject AddLocalTemplate( 

   FunctionDefinition pFunctionDefinition

)

public:

StorableObject^ AddLocalTemplate( 

   FunctionDefinition^ pFunctionDefinition

)


#### Parameters

*pFunctionDefinition*
:   Function definition from which a local template is created.

#### Return Value

Returns new template created based on passed function definition.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if parameter is `null`. |
| [System.InvalidOperationException](#) | Thrown when [SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~SegmentTemplate.html) is assigned. |

Remarks

If [SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~SegmentTemplate.html) is assigned then local template are taken from specification and can't be changed.
