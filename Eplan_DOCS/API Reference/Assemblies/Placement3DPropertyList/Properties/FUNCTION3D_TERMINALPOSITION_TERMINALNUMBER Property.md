# FUNCTION3D_TERMINALPOSITION_TERMINALNUMBER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic693.html

---

Connection point pattern: Terminal designation # 36071.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_TERMINALNUMBER( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_TERMINALNUMBER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Terminal designation, used in the connection point patterns of topology functions.
