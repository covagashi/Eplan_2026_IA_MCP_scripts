# GetSegmentDefinitions Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetSegmentDefinitions.html

---

Returns [Eplan.EplApi.DataModel.Planning.SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html) matching the given filter.

Syntax

**C#**



public SegmentDefinition[] GetSegmentDefinitions( 

   SegmentDefinitionsFilter pFilter

)

public:

array<SegmentDefinition^>^ GetSegmentDefinitions( 

   SegmentDefinitionsFilter^ pFilter

)


#### Parameters

*pFilter*
:   Object used cusomize the results. If `null` then all segment definitions for current project are returned.

#### Return Value

Array of [Eplan.EplApi.DataModel.Planning.SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html) matching the filter.

Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown if DMObjectsFinder is not correctly initialized. |
