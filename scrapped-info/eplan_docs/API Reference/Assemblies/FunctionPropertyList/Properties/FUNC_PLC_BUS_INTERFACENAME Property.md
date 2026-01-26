# FUNC_PLC_BUS_INTERFACENAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLC_BUS_INTERFACENAME().html

---

Bus interface: Name # 20447.

Syntax

**C#**



public PropertyValue FUNC_PLC_BUS_INTERFACENAME {get; set;}

public:

property PropertyValue^ FUNC_PLC_BUS_INTERFACENAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The bus interface name serves to group bus ports for the export of Ethernet-based bus systems. Associated bus ports are combined into a logical unit via this name.
