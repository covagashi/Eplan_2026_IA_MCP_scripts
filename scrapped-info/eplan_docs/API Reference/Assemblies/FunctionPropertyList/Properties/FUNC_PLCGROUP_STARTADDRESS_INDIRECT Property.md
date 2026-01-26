# FUNC_PLCGROUP_STARTADDRESS_INDIRECT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCGROUP_STARTADDRESS_INDIRECT().html

---

Start address of PLC card (indirect) # 20423.

Syntax

**C#**



public PropertyValue FUNC_PLCGROUP_STARTADDRESS_INDIRECT {get; set;}

public:

property PropertyValue^ FUNC_PLCGROUP_STARTADDRESS_INDIRECT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the start address entered for the relevant PLC box for a PLC connection point. The value entered defines the start value for the address range of a PLC card; this is taken into account for automatic addressing.
