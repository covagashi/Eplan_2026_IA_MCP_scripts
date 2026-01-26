# SetFilteredPropertyList Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectsFilter~SetFilteredPropertyList.html

---

Sets the [StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html) that [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s matching the filter must have.

Syntax

**C#**



public void SetFilteredPropertyList( 

   StorableObjectPropertyList searchedPropList

)

public:

void SetFilteredPropertyList( 

   StorableObjectPropertyList^ searchedPropList

)


#### Parameters

*searchedPropList*
:   List of the P8 properties the [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s matching the the filter. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
