# FUNC_PLCGROUP_STARTADDRESS_8_OUTPUTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCGROUP_STARTADDRESS_8_OUTPUTS().html

---

PLC subdevice 8: Start address (outputs) # 20516.

Syntax

**C#**



public PropertyValue FUNC_PLCGROUP_STARTADDRESS_8_OUTPUTS {get; set;}

public:

property PropertyValue^ FUNC_PLCGROUP_STARTADDRESS_8_OUTPUTS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Start address for the outputs of the PLC subdevice 8 (for PLC data exchange in AutomationML AR APC format). Can be used in the addressing format.
