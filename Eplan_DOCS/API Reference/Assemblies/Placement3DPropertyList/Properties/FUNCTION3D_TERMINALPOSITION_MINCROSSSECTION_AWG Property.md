# FUNCTION3D_TERMINALPOSITION_MINCROSSSECTION_AWG Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic681.html

---

Connection point pattern: Min. AWG # 36077.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_MINCROSSSECTION_AWG( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_MINCROSSSECTION_AWG {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Minimum connection cross-section to be connected for a connection point in the connection point pattern.
