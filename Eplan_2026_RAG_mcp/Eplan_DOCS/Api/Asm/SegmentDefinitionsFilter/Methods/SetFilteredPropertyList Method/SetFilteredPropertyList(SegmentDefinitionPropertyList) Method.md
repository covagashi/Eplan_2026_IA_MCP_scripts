# SetFilteredPropertyList(SegmentDefinitionPropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic460.html

---

Sets the [Eplan.EplApi.DataModel.Planning.SegmentDefinitionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinitionPropertyList.html) that [Eplan.EplApi.DataModel.Planning.SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html)s matching the filter must have.

Syntax

**C#**



public void SetFilteredPropertyList( 

   SegmentDefinitionPropertyList searchedPropList

)

public:

void SetFilteredPropertyList( 

   SegmentDefinitionPropertyList^ searchedPropList

)


#### Parameters

*searchedPropList*
:   List of the P8 properties the [Eplan.EplApi.DataModel.Planning.SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html)s matching the the filter. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
