# CABLINGSEGMENT_DUCT_TYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.SegmentPropertyList~CABLINGSEGMENT_DUCT_TYPE().html

---

Topology: Routing path type (routing path) # 20345.

Syntax

**C#**



public PropertyValue CABLINGSEGMENT_DUCT_TYPE {get; set;}

public:

property PropertyValue^ CABLINGSEGMENT_DUCT_TYPE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Specifies the way in which connections or cables are routed in this routing path (for example pipe, cable duct, cable platform, etc.). This results in the routing path type of the connections / cables that are routed in this routing path (property Topology: Routing path types (ID 20344)).
