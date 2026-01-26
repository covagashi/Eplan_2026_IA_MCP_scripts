# FUNC_PLCSTATIONNAME_INDIRECT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~FUNC_PLCSTATIONNAME_INDIRECT().html

---

PLC station: ID (indirect) # 20420.

Syntax

**C#**



public PropertyValue FUNC_PLCSTATIONNAME_INDIRECT {get; set;}

public:

property PropertyValue^ FUNC_PLCSTATIONNAME_INDIRECT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Outputs the station ID of the CPU for the PLC box to which the PLC connection point is assigned.
