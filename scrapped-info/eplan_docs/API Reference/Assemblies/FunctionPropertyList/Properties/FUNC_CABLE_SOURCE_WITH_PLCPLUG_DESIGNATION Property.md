# FUNC_CABLE_SOURCE_WITH_PLCPLUG_DESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_CABLE_SOURCE_WITH_PLCPLUG_DESIGNATION().html

---

Cables: Source (with plug designation) # 20383.

Syntax

**C#**



public PropertyValue FUNC_CABLE_SOURCE_WITH_PLCPLUG_DESIGNATION {get; set;}

public:

property PropertyValue^ FUNC_CABLE_SOURCE_WITH_PLCPLUG_DESIGNATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Shows the source of the cable with plug designation. At bus ports the bus interface name of the bus port is displayed in addition to the plug designation. The property can be used for the display in the schematic as well as in block properties, at external editing and in reports.
