# FUNC_PLCGROUP_STARTADDRESS_2 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCGROUP_STARTADDRESS_2().html

---

Start address 2 of PLC card # 20255.

Syntax

**C#**



public PropertyValue FUNC_PLCGROUP_STARTADDRESS_2 {get; set;}

public:

property PropertyValue^ FUNC_PLCGROUP_STARTADDRESS_2 {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

For PLC cards that have both inputs and outputs, you can use this property to specify a separate start address for the address range of the outputs. This way, inputs and outputs can be addressed separately. The start address specifies the start value for the address range of a PLC card; this is taken into account for automatic addressing. The property is entered on the "PLC box" tab of the property dialog. For this property to be used, the Separate address range for inputs and outputs check box must be deactivated in the PLC-specific settings.
