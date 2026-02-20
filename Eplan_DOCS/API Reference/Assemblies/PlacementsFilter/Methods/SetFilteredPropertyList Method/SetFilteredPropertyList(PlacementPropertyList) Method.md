# SetFilteredPropertyList(PlacementPropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementsFilter~SetFilteredPropertyList(PlacementPropertyList).html

---

Sets the [PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html) that [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s matching the filter must have.

Syntax

**C#**



public void SetFilteredPropertyList( 

   PlacementPropertyList searchedPropList

)

public:

void SetFilteredPropertyList( 

   PlacementPropertyList^ searchedPropList

)


#### Parameters

*searchedPropList*
:   List of the P8 properties the [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s matching the the filter. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
