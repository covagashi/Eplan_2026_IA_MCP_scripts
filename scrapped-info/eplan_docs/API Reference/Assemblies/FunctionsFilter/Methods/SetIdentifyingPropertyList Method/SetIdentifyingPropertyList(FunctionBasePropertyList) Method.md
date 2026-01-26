# SetIdentifyingPropertyList(FunctionBasePropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~SetIdentifyingPropertyList(FunctionBasePropertyList).html

---

Sets the [FunctionBasePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList.html) that identifies the matching [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s.

Syntax

**C#**



public void SetIdentifyingPropertyList( 

   FunctionBasePropertyList identPropList

)

public:

void SetIdentifyingPropertyList( 

   FunctionBasePropertyList^ identPropList

)


#### Parameters

*identPropList*
:   List of the properties which are identifying the matching [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
