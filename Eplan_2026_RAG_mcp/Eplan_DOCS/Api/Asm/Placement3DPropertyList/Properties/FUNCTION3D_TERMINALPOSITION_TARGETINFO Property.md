# FUNCTION3D_TERMINALPOSITION_TARGETINFO Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic692.html

---

Connection point pattern: Internal / External index # 36070.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_TARGETINFO( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_TARGETINFO {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Defines for a connection point in the connection point pattern the number of the internal or external connection point that this connection point represents.
