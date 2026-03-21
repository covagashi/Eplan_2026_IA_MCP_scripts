# FUNC_PLC_BUS_INTERFACENAME_MASTER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLC_BUS_INTERFACENAME_MASTER().html

---

Bus interface: Main bus port # 20448.

Syntax

**C#**



public PropertyValue FUNC_PLC_BUS_INTERFACENAME_MASTER {get; set;}

public:

property PropertyValue^ FUNC_PLC_BUS_INTERFACENAME_MASTER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Identifies a bus port within an interface as the main bus port. This bus port represents the bus interface and bears the data. During exporting the data are read from the main bus port and written into the PLC configuration file.
