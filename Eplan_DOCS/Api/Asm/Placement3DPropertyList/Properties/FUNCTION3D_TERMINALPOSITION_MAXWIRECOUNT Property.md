# FUNCTION3D_TERMINALPOSITION_MAXWIRECOUNT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic679.html

---

Connection point pattern: Max. number of connections # 36064.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_MAXWIRECOUNT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_MAXWIRECOUNT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Maximum number of connections that can be connected to the connection point; defined in the connection point pattern.
