# FUNC_PLCGROUP_STARTADDRESS_2_OUTPUTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCGROUP_STARTADDRESS_2_OUTPUTS().html

---

PLC subdevice 2: Start address (outputs) # 20455.

Syntax

**C#**



public PropertyValue FUNC_PLCGROUP_STARTADDRESS_2_OUTPUTS {get; set;}

public:

property PropertyValue^ FUNC_PLCGROUP_STARTADDRESS_2_OUTPUTS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Start address for the outputs of the PLC subdevice 2 (for PLC data exchange in AutomationML AR APC format). Can be used in the addressing format. PLC devices exist that consist of several integrated modules and that have several start addresses. Such a device can consist, for example, of an internal CPU module, an internal input-output module as well as internal counter module - however with only one part number. Such integrated modules within a PLC device can be displayed in Eplan with PLC subdevices. To this purpose up to twelve PLC subdevices are available.
