# SetFilteredPropertyList Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionsFilter~SetFilteredPropertyList.html

---

Sets the [ConnectionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList.html) that [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s matching the filter must have.

Syntax

**C#**



public void SetFilteredPropertyList( 

   ConnectionPropertyList searchedPropList

)

public:

void SetFilteredPropertyList( 

   ConnectionPropertyList^ searchedPropList

)


#### Parameters

*searchedPropList*
:   List of the P8 properties the [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s matching the the filter. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
