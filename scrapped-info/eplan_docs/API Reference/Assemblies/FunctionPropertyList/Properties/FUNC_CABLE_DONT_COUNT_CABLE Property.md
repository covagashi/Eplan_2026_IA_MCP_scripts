# FUNC_CABLE_DONT_COUNT_CABLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_CABLE_DONT_COUNT_CABLE().html

---

Do not use cable when adding up cable lengths # 20060.

Syntax

**C#**



public PropertyValue FUNC_CABLE_DONT_COUNT_CABLE {get; set;}

public:

property PropertyValue^ FUNC_CABLE_DONT_COUNT_CABLE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Omits the cable from the summing of the cable lengths.
