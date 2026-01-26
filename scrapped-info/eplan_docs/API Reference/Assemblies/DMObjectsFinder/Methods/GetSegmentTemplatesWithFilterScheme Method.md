# GetSegmentTemplatesWithFilterScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetSegmentTemplatesWithFilterScheme.html

---

Returns [Eplan.EplApi.DataModel.Planning.SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplate.html) matching the given filter.

Syntax

**C#**



public SegmentTemplate[] GetSegmentTemplatesWithFilterScheme( 

   string strSchemeName

)

public:

array<SegmentTemplate^>^ GetSegmentTemplatesWithFilterScheme( 

   String^ strSchemeName

)


#### Parameters

*strSchemeName*
:   Name of the scheme used to filter out results. If `null` or empty then all segment templates for current project are returned.

#### Return Value

Array of [Eplan.EplApi.DataModel.Planning.SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplate.html).

Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown if DMObjectsFinder is not correctly initialized. |
| [System.ArgumentException](#) | Thrown if filter scheme does not exist. |
