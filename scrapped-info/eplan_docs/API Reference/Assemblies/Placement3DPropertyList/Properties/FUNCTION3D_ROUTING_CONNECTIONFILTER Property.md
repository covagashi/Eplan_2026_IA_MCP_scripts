# FUNCTION3D_ROUTING_CONNECTIONFILTER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_ROUTING_CONNECTIONFILTER().html

---

Layout space: Connection filter # 36026.

Syntax

**C#**



public PropertyValue FUNCTION3D_ROUTING_CONNECTIONFILTER {get; set;}

public:

property PropertyValue^ FUNCTION3D_ROUTING_CONNECTIONFILTER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Filter for generating routing path networks. Is used for routing to control which connections may be routed along which routing tracks (channel, manual routing path, routing range, wiring cut-out). Connection filters are taken into account only if the "Layout space: Routing track specification" (ID 31094) property has not been activated.
