# SetIdentifyingPropertyList(FunctionPropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionsFilter~SetIdentifyingPropertyList(FunctionPropertyList).html

---

Sets the [FunctionPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList.html) that identifies the matching [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s.

Syntax

**C#**



public void SetIdentifyingPropertyList( 

   FunctionPropertyList identPropList

)

public:

void SetIdentifyingPropertyList( 

   FunctionPropertyList^ identPropList

)


#### Parameters

*identPropList*
:   List of the properties which are identifying the matching [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |

Example

The following example shows how to filter by identifying name.

**C#**

```


private Function[] GetSubFunctions(Function oFunction)

{

    FunctionBasePropertyList oIdentNameProps = oFunction.IdentifyingNameParts;

    FunctionPropertyList oFilterOutMainProps = new FunctionPropertyList();

    oFilterOutMainProps.FUNC_MAINFUNCTION = false;

    DMObjectsFinder oFinder = new DMObjectsFinder(m_oProject);

    FunctionsFilter oFilter = new FunctionsFilter();

    oFilter.SetIdentifyingPropertyList(oIdentNameProps);

    oFilter.SetFilteredPropertyList(oFilterOutMainProps);

    Function[] oResult = oFinder.GetFunctions(oFilter);

    return oResult;

}

```
