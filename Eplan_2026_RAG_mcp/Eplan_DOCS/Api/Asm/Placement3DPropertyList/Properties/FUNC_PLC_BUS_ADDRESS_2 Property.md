# FUNC_PLC_BUS_ADDRESS_2 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLC_BUS_ADDRESS_2().html

---

Physical network: Bus ID / item number 2 # 20386.

Syntax

**C#**



public PropertyValue FUNC_PLC_BUS_ADDRESS_2 {get; set;}

public:

property PropertyValue^ FUNC_PLC_BUS_ADDRESS_2 {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Second bus ID of the bus port. The property in the "Bus data" tab of the property dialog is entered at the network / bus cable-connection points. Describes the additional address / position the bus master uses to manage a bus port. The property is taken into consideration during the PLC data exchange in AutomationML AR APC format.
