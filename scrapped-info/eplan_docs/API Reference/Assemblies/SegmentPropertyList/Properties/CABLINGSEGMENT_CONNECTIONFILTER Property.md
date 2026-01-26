# CABLINGSEGMENT_CONNECTIONFILTER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.SegmentPropertyList~CABLINGSEGMENT_CONNECTIONFILTER().html

---

Topology: Connection filter # 20247.

Syntax

**C#**



public PropertyValue CABLINGSEGMENT_CONNECTIONFILTER {get; set;}

public:

property PropertyValue^ CABLINGSEGMENT_CONNECTIONFILTER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Filter for generating routing path networks. Is used during routing to control which connections may be routed through which routing track (routing paths and routing points). Connection filters are taken into account only if the "Topology: Routing track specification" (ID 31119) property has not been activated.
