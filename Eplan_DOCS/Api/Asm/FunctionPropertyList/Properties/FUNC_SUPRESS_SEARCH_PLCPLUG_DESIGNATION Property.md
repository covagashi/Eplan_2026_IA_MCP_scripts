# FUNC_SUPRESS_SEARCH_PLCPLUG_DESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_SUPRESS_SEARCH_PLCPLUG_DESIGNATION().html

---

Plug designation (automatic): Suppress search # 20579.

Syntax

**C#**



public PropertyValue FUNC_SUPRESS_SEARCH_PLCPLUG_DESIGNATION {get; set;}

public:

property PropertyValue^ FUNC_SUPRESS_SEARCH_PLCPLUG_DESIGNATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Prevents the automatic assignment of a plug designation. If this property is activated at a PLC connection point, the Plug designation (automatic) property remains empty, in as far as no manual value was entered for the plug designation.
