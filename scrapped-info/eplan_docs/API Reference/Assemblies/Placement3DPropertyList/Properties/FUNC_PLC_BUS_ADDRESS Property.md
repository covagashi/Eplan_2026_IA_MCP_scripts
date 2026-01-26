# FUNC_PLC_BUS_ADDRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLC_BUS_ADDRESS().html

---

Physical network: Bus ID / item number # 20311.

Syntax

**C#**



public PropertyValue FUNC_PLC_BUS_ADDRESS {get; set;}

public:

property PropertyValue^ FUNC_PLC_BUS_ADDRESS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Bus ID of the bus port. Depending on the bus system, the value is a simple number, an IP address or a combination of letters and numbers. The property in the "Bus data" tab of the property dialog is entered at the network / bus cable-connection points. Describes the address / position the bus master uses to manage a bus port.
