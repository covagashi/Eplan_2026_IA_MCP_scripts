# FUNCTION3D_TERMINALPOSITION_CLAMPSPACE_OFFSET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic668.html

---

Clamping space offset # 36086.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_CLAMPSPACE_OFFSET( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_CLAMPSPACE_OFFSET {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Describes the offset of the clamping space from the item edge into the item.
