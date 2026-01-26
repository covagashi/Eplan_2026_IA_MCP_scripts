# FUNC_TERMINALLEVEL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_TERMINALLEVEL().html

---

Level # 20034.

Syntax

**C#**



public PropertyValue FUNC_TERMINALLEVEL {get; set;}

public:

property PropertyValue^ FUNC_TERMINALLEVEL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Level of the multi-level terminal; if the value is "0", then there are no multi-level terminals, but a terminal with only one level.
