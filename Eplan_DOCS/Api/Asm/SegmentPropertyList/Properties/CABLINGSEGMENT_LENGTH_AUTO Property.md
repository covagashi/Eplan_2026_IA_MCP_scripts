# CABLINGSEGMENT_LENGTH_AUTO Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.SegmentPropertyList~CABLINGSEGMENT_LENGTH_AUTO().html

---

Topology: Routing length (automatic) # 20250.

Syntax

**C#**



public PropertyValue CABLINGSEGMENT_LENGTH_AUTO {get; set;}

public:

property PropertyValue^ CABLINGSEGMENT_LENGTH_AUTO {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Length of a routing path or routing point. Is used during routing to calculate the precise length of the associated connection. Shows the content of the manually entered routing length or, when that is empty, the geometric length.
