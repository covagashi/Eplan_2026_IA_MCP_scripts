# FUNC_POTENTIALTYPE_TERMINALPOINTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_POTENTIALTYPE_TERMINALPOINTS().html

---

Potential type of connection points # 20166.

Syntax

**C#**



public PropertyValue FUNC_POTENTIALTYPE_TERMINALPOINTS {get; set;}

public:

property PropertyValue^ FUNC_POTENTIALTYPE_TERMINALPOINTS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Provides the potential type of the connection points, when this is the same for all function connection points. Otherwise the "Undefined" potential type is output instead.
