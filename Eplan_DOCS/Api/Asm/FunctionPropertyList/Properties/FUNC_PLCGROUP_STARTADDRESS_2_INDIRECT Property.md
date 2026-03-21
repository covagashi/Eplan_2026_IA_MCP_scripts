# FUNC_PLCGROUP_STARTADDRESS_2_INDIRECT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCGROUP_STARTADDRESS_2_INDIRECT().html

---

Start address 2 of PLC card (indirect) # 20298.

Syntax

**C#**



public PropertyValue FUNC_PLCGROUP_STARTADDRESS_2_INDIRECT {get; set;}

public:

property PropertyValue^ FUNC_PLCGROUP_STARTADDRESS_2_INDIRECT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the optional second start address entered at the relevant PLC box for a PLC connection point. For PLC cards that have both inputs and outputs, you can specify a separate start address for the outputs. The value entered defines the start value for the address range of the outputs of a PLC card; this is taken into account for automatic addressing.
