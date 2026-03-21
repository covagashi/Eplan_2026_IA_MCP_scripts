# SetFilteredPropertyList(FunctionPropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~SetFilteredPropertyList(FunctionPropertyList).html

---

Sets the [FunctionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html) that [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching the filter must have.

Syntax

**C#**



public void SetFilteredPropertyList( 

   FunctionPropertyList searchedPropList

)

public:

void SetFilteredPropertyList( 

   FunctionPropertyList^ searchedPropList

)


#### Parameters

*searchedPropList*
:   List of the P8 properties the [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching the the filter. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
