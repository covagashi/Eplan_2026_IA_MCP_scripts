# FUNCTION3D_TERMINALPOSITION_CONTACTTYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic672.html

---

Connection point pattern: Wire termination processing (Eplan Cabinet) # 36061.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_CONTACTTYPE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_CONTACTTYPE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

This property is only required for reasons of compatibility with Eplan Cabinet. For a connection point, this shows how the end of the connection is handled, for example with stripping or crimping. Is selected from a drop-down list in parts management on the Connection points tab where user-defined values can also be assigned.
