# FUNCTION3D_TERMINALPOSITION_HOLEDIAMETER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic675.html

---

Shaft diameter # 36087.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_HOLEDIAMETER( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_HOLEDIAMETER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

The shaft diameter describes the size of the hole in which the terminal screw sits. Entry for example "5 mm".
