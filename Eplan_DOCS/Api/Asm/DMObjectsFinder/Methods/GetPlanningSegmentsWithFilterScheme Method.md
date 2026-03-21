# GetPlanningSegmentsWithFilterScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlanningSegmentsWithFilterScheme.html

---

Returns [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) matching the given filter.

Syntax

**C#**



public PlanningSegment[] GetPlanningSegmentsWithFilterScheme( 

   string strSchemeName

)

public:

array<PlanningSegment^>^ GetPlanningSegmentsWithFilterScheme( 

   String^ strSchemeName

)


#### Parameters

*strSchemeName*
:   Name of the scheme used to filter out results. If `null` or empty then all planning segments for current project are returned.

#### Return Value

Array of [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html).

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown if filter scheme does not exist. |
| [System.InvalidOperationException](#) | Thrown if DMObjectsFinder is not correctly initialized. |
