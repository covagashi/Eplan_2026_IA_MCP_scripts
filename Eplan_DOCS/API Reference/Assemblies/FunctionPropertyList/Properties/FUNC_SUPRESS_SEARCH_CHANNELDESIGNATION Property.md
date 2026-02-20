# FUNC_SUPRESS_SEARCH_CHANNELDESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_SUPRESS_SEARCH_CHANNELDESIGNATION().html

---

Channel designation (automatic): Suppress search # 20578.

Syntax

**C#**



public PropertyValue FUNC_SUPRESS_SEARCH_CHANNELDESIGNATION {get; set;}

public:

property PropertyValue^ FUNC_SUPRESS_SEARCH_CHANNELDESIGNATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Prevents the automatic assignment of a channel designation. If this property is activated at a PLC connection point, the Channel designation (automatic) property remains empty, in as far as no manual value was entered for the channel designation.
