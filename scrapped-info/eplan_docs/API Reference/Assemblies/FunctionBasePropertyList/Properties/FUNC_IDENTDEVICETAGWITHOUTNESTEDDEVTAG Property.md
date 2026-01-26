# FUNC_IDENTDEVICETAGWITHOUTNESTEDDEVTAG Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList~FUNC_IDENTDEVICETAGWITHOUTNESTEDDEVTAG().html

---

DT (identifying, without subordinate DT) # 20007.

Syntax

**C#**



public PropertyValue FUNC_IDENTDEVICETAGWITHOUTNESTEDDEVTAG {get; set;}

public:

property PropertyValue^ FUNC_IDENTDEVICETAGWITHOUTNESTEDDEVTAG {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the identifying device tag without the subordinate DT. The property is used in the navigator in the tree view.

Example: "=A+O-U1" is output for "=A+O-U1-K1".
