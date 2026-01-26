# IdentifyingNameParts Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~IdentifyingNameParts.html

---

Returns identifying name of the Function.

Syntax

**C#**



public virtual FunctionBasePropertyList IdentifyingNameParts {get;}

public:

virtual property FunctionBasePropertyList^ IdentifyingNameParts {

   FunctionBasePropertyList^ get();

}


#### Property Value

Identifying name of the Function by FunctionBasePropertyList.

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
