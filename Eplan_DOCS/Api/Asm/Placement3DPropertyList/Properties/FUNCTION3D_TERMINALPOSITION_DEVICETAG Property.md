# FUNCTION3D_TERMINALPOSITION_DEVICETAG Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic673.html

---

Connection point pattern: Plug designation # 36068.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_DEVICETAG( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_DEVICETAG {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Plug designation of the connection point in the connection point pattern.
