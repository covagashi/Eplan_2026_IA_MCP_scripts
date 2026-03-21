# FUNCTION3D_ROUTING_SEGMENT_LENGTH_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic662.html

---

Routing path / Curve: Length (automatic) # 36028.

Syntax

**C#**



public PropertyValue FUNCTION3D_ROUTING_SEGMENT_LENGTH_AUTOMATIC {get; set;}

public:

property PropertyValue^ FUNCTION3D_ROUTING_SEGMENT_LENGTH_AUTOMATIC {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only..

Length of a routing path or curve placed in the layout space. Is used during routing to calculate the precise length of the associated connection. Shows the content of the manually entered length or, when that is empty, the geometric length in the layout space.
