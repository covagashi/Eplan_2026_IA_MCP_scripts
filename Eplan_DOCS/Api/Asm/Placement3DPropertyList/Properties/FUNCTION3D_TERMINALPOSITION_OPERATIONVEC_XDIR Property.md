# FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_XDIR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic683.html

---

X vector: Tool # 36091.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_XDIR( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_XDIR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

The properties for the vector of the tool describe the position and the screwing direction of a terminal screw in an item with screwed connection. Entry for example "-1".
