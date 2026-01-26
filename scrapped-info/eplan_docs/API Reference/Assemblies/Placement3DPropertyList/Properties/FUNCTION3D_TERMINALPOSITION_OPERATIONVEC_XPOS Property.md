# FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_XPOS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic684.html

---

X position: Tool # 36088.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_XPOS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_XPOS {

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
