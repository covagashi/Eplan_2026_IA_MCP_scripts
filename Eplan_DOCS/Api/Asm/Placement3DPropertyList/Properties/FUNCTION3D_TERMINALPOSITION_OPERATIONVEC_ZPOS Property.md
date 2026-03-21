# FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_ZPOS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic688.html

---

Z position: Tool # 36090.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_ZPOS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_ZPOS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

The properties for specifying coordinate values for the position of the tool describe the position of a terminal screw in an item with screw connection. Entry for example "12 mm".
