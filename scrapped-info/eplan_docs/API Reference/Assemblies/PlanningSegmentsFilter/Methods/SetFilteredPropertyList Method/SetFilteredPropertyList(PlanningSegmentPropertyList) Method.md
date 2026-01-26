# SetFilteredPropertyList(PlanningSegmentPropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic418.html

---

Sets the [Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList.html) that [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)s matching the filter must have.

Syntax

**C#**



public void SetFilteredPropertyList( 

   PlanningSegmentPropertyList searchedPropList

)

public:

void SetFilteredPropertyList( 

   PlanningSegmentPropertyList^ searchedPropList

)


#### Parameters

*searchedPropList*
:   List of the P8 properties the [Eplan.EplApi.DataModel.Planning.PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment.html)s matching the the filter. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
