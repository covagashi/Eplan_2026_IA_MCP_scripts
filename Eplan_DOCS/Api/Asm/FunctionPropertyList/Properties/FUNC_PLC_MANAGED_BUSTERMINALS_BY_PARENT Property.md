# FUNC_PLC_MANAGED_BUSTERMINALS_BY_PARENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLC_MANAGED_BUSTERMINALS_BY_PARENT().html

---

Manage bus ports at the superior device # 20620.

Syntax

**C#**



public PropertyValue FUNC_PLC_MANAGED_BUSTERMINALS_BY_PARENT {get; set;}

public:

property PropertyValue^ FUNC_PLC_MANAGED_BUSTERMINALS_BY_PARENT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property can be used to manage all the bus ports of the device and the plugged-in devices together for devices into which further devices are plugged. To do so activate this property at the PLC boxes of the plugged-in devices. The superior device and the associated plugged-in devices are identified by means of the properties Rack and PLC card is placed on rack ID.
