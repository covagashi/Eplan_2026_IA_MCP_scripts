# FUNC_PLCSTATIONNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCSTATIONNAME().html

---

PLC station: ID # 20408.

Syntax

**C#**



public PropertyValue FUNC_PLCSTATIONNAME {get; set;}

public:

property PropertyValue^ FUNC_PLCSTATIONNAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

PLC station ID at the PLC box. The station ID is used as a grouping element for the network components. As a rule it is assigned depending on the physical place (enclosure, switch box etc.) of the network components.
