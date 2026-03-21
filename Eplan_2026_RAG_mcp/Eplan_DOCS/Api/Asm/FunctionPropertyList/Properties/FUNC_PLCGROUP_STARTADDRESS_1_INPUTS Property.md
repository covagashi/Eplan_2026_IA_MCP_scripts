# FUNC_PLCGROUP_STARTADDRESS_1_INPUTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCGROUP_STARTADDRESS_1_INPUTS().html

---

PLC subdevice 1: Start address (inputs) # 20609.

Syntax

**C#**



public PropertyValue FUNC_PLCGROUP_STARTADDRESS_1_INPUTS {get; set;}

public:

property PropertyValue^ FUNC_PLCGROUP_STARTADDRESS_1_INPUTS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Start address for the inputs of the PLC subdevice 1 (for PLC data exchange in AutomationML AR APC format). Can be used in the addressing format. PLC devices exist that consist of several integrated modules and that have several start addresses. Such a device can consist, for example, of an internal CPU module, an internal input-output module as well as internal counter module - however with only one part number. Such integrated modules within a PLC device can be displayed in Eplan with PLC subdevices. To this purpose up to twelve PLC subdevices are available.
