# FUNCTION3D_TERMINALPOSITION_XDIR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_TERMINALPOSITION_XDIR(Int32).html

---

Connection point pattern: X vector # 36072.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_XDIR( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_XDIR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

X-vector of the connection point direction in the connection point pattern.
