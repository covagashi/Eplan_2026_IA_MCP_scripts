# FUNC_PLCSAFETYADDRESS_1 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCSAFETYADDRESS_1().html

---

PLC subdevice 1: Safety address: Target # 20622.

Syntax

**C#**



public PropertyValue FUNC_PLCSAFETYADDRESS_1 {get; set;}

public:

property PropertyValue^ FUNC_PLCSAFETYADDRESS_1 {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Safety address at PLC subdevices of safety modules (for example F-address for PROFIsafe). In general this value is entered at the modules that are participants of a safety network. Detailed information on this is available from the PLC manufacturer. The properties for the safety addresses at PLC subdevices are taken into consideration for the PLC data exchange as of the AutomationML AR APC Version 1.1.0.
