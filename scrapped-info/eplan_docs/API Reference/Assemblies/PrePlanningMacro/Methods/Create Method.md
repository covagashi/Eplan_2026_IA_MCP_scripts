# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PrePlanningMacro~Create.html

---

Creates file and writes a pre-planning macro from planning segments and their sub objects.

Syntax

**C#**



public void Create( 

   IEnumerable<PlanningSegment> colSegments,

   string strMacroFileName,

   MultiLangString pDescription

)

public:

void Create( 

   IEnumerable<PlanningSegment^>^ colSegments,

   String^ strMacroFileName,

   MultiLangString^ pDescription

)


#### Parameters

*colSegments*
:   Collection of segments. Can't be `null`.

*strMacroFileName*
:   Filename (inclusive path information and type) of the macro. Can't be `null`.

*pDescription*
:   Description of macro. If `null` then description is empty.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when parameters are not valid. |
| [System.NotImplementedException](#) | Thrown when internal error occured while creating macro. |
| [Eplan.EplApi.DataModel.ObjectNotCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectNotCreatedException.html) | Thrown when macro has not been created. |
