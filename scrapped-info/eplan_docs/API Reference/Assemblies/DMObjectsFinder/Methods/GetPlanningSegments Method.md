# GetPlanningSegments Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPlanningSegments.html

---

Returns [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) matching the given filter.

Syntax

**C#**



public PlanningSegment[] GetPlanningSegments( 

   PlanningSegmentsFilter pFilter

)

public:

array<PlanningSegment^>^ GetPlanningSegments( 

   PlanningSegmentsFilter^ pFilter

)


#### Parameters

*pFilter*
:   Object used cusomize the results. If `null` then all planning segments for current project are returned.

#### Return Value

Array of [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html) matching the filter.

Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown if DMObjectsFinder is not correctly initialized. |
