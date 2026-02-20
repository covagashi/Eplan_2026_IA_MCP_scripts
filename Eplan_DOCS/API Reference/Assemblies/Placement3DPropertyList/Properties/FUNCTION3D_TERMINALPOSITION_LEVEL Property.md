# FUNCTION3D_TERMINALPOSITION_LEVEL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_TERMINALPOSITION_LEVEL(Int32).html

---

Connection point pattern: Level # 36069.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_LEVEL( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_LEVEL {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Level of the connection point (if it is a terminal) in the connection point pattern.
