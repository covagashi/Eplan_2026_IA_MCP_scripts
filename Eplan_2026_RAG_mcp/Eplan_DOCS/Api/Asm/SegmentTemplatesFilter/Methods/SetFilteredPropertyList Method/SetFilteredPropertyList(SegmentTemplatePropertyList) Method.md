# SetFilteredPropertyList(SegmentTemplatePropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic462.html

---

Sets the [Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList.html) that [Eplan.EplApi.DataModel.Planning.SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplate.html)s matching the filter must have.

Syntax

**C#**



public void SetFilteredPropertyList( 

   SegmentTemplatePropertyList searchedPropList

)

public:

void SetFilteredPropertyList( 

   SegmentTemplatePropertyList^ searchedPropList

)


#### Parameters

*searchedPropList*
:   List of the P8 properties the [Eplan.EplApi.DataModel.Planning.SegmentTemplate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplate.html)s matching the the filter. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
