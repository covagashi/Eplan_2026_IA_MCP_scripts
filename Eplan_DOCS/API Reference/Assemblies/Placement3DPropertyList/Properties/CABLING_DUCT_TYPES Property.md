# CABLING_DUCT_TYPES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~CABLING_DUCT_TYPES().html

---

Topology: Routing path types # 20344.

Syntax

**C#**



public PropertyValue CABLING_DUCT_TYPES {get; set;}

public:

property PropertyValue^ CABLING_DUCT_TYPES {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only..

This property outputs the routing path types of the routing paths that a connection routed in the routing path network or a routed cable runs through.
