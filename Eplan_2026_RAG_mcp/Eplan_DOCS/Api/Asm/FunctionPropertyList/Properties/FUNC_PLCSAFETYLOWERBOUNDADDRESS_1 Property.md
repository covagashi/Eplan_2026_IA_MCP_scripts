# FUNC_PLCSAFETYLOWERBOUNDADDRESS_1 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCSAFETYLOWERBOUNDADDRESS_1().html

---

PLC subdevice 1: Safety address: Lower value # 20658.

Syntax

**C#**



public PropertyValue FUNC_PLCSAFETYLOWERBOUNDADDRESS_1 {get; set;}

public:

property PropertyValue^ FUNC_PLCSAFETYLOWERBOUNDADDRESS_1 {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Safety address (lower value) at PLC subdevices of safety modules. Detailed information on this is available from the PLC manufacturer. The value itself is entered during the import of PLC configuration files in the AutomationML AR APC format. The properties for the safety addresses at PLC subdevices are taken into consideration for the PLC data exchange as of the AutomationML AR APC Version 1.1.0.
