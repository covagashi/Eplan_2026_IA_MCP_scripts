# FUNC_PLCSAFETYUPPERBOUNDADDRESS_1 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCSAFETYUPPERBOUNDADDRESS_1().html

---

PLC subdevice 1: Safety address: Upper value # 20646.

Syntax

**C#**



public PropertyValue FUNC_PLCSAFETYUPPERBOUNDADDRESS_1 {get; set;}

public:

property PropertyValue^ FUNC_PLCSAFETYUPPERBOUNDADDRESS_1 {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Safety address (upper value) at PLC subdevices of safety modules. Detailed information on this is available from the PLC manufacturer. The value itself is entered during the import of PLC configuration files in the AutomationML AR APC format. The properties for the safety addresses at PLC subdevices are taken into consideration for the PLC data exchange as of the AutomationML AR APC Version 1.1.0.
