# FUNC_PLCBUSINTERFACENAME_AND_PLCPLUG Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCBUSINTERFACENAME_AND_PLCPLUG().html

---

Bus interface: Name (with plug designation) # 20443.

Syntax

**C#**



public PropertyValue FUNC_PLCBUSINTERFACENAME_AND_PLCPLUG {get; set;}

public:

property PropertyValue^ FUNC_PLCBUSINTERFACENAME_AND_PLCPLUG {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Composite property from bus interface name and plug designation, without a separator. The property supports the identification of bus ports.
