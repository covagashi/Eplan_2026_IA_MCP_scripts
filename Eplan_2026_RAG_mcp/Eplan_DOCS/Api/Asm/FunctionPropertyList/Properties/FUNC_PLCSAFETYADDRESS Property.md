# FUNC_PLCSAFETYADDRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCSAFETYADDRESS().html

---

Safety address: Target # 20439.

Syntax

**C#**



public PropertyValue FUNC_PLCSAFETYADDRESS {get; set;}

public:

property PropertyValue^ FUNC_PLCSAFETYADDRESS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Safety address at safety modules (for example F-address for PROFIsafe). In general this value is entered at the modules that are participants of a safety network. Detailed information on this is available from the PLC manufacturer. The properties for the safety addresses are taken into consideration for the PLC data exchange as of AutomationML AR APC Version 1.1.0.
