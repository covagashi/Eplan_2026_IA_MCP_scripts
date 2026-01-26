# CABLINGSEGMENT_CROSSSECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.SegmentPropertyList~CABLINGSEGMENT_CROSSSECTION().html

---

Topology: Routing path cross-section # 20248.

Syntax

**C#**



public PropertyValue CABLINGSEGMENT_CROSSSECTION {get; set;}

public:

property PropertyValue^ CABLINGSEGMENT_CROSSSECTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Indicates the fill capacity of the routing path, and serves as a basis for calculating the fill capacity. If no routing path cross-section is entered, the fill capacity will not be calculated either.
