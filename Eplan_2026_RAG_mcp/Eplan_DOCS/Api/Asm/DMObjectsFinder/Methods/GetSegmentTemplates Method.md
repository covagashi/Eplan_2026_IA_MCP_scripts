# GetSegmentTemplates Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetSegmentTemplates.html

---

Returns [Eplan.EplApi.DataModel.Planning.SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplate.html) matching the given filter.

Syntax

**C#**



public SegmentTemplate[] GetSegmentTemplates( 

   SegmentTemplatesFilter pFilter

)

public:

array<SegmentTemplate^>^ GetSegmentTemplates( 

   SegmentTemplatesFilter^ pFilter

)


#### Parameters

*pFilter*
:   Object used cusomize the results. If `null` then all segment templates for current project are returned.

#### Return Value

Array of [Eplan.EplApi.DataModel.Planning.SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplate.html) matching the filter.

Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown if DMObjectsFinder is not correctly initialized. |
