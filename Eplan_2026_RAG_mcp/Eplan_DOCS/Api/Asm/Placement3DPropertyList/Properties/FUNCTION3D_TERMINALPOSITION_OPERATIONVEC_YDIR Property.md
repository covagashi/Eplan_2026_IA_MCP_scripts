# FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_YDIR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic685.html

---

Y vector: Tool # 36092.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_YDIR( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_OPERATIONVEC_YDIR {

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
