# FUNCTION3D_TERMINALPOSITION_TWINSLEEVE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic695.html

---

Connection point pattern: Dual sleeve prescribed # 36065.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_TWINSLEEVE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_TWINSLEEVE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Specifies for a connection point in the connection point pattern that dual sleeves are to be used if two connections lead to this connection point.
