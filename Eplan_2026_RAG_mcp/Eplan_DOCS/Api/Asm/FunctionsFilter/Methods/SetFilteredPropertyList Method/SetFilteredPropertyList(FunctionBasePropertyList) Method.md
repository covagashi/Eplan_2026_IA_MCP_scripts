# SetFilteredPropertyList(FunctionBasePropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~SetFilteredPropertyList(FunctionBasePropertyList).html

---

Sets the [FunctionBasePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList.html) that [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching the filter must have.

Syntax

**C#**



public void SetFilteredPropertyList( 

   FunctionBasePropertyList searchedPropList

)

public:

void SetFilteredPropertyList( 

   FunctionBasePropertyList^ searchedPropList

)


#### Parameters

*searchedPropList*
:   List of the P8 properties the [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching the the filter. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
