# FUNCTION3D_TERMINALPOSITION_PLC_BUS_INTERFACENAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic689.html

---

Connection point pattern: Bus interface name # 36101.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_PLC_BUS_INTERFACENAME( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_PLC_BUS_INTERFACENAME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Bus interface name of the connection point in the connection point pattern.
