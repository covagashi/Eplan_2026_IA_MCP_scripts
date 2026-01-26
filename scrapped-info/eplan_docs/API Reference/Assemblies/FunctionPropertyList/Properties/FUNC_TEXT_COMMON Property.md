# FUNC_TEXT_COMMON Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_TEXT_COMMON().html

---

Function text (common) # 20120.

Syntax

**C#**



public PropertyValue FUNC_TEXT_COMMON {get; set;}

public:

property PropertyValue^ FUNC_TEXT_COMMON {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only..

Displays the function text (automatic) of the function or, if it is empty, the function text (automatic) of the associated main function.
