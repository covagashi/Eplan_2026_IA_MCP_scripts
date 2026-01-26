# FUNC_CABLE_DESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_CABLE_DESIGNATION().html

---

Cable / Conduit: Designation in graphic # 20067.

Syntax

**C#**



public PropertyValue FUNC_CABLE_DESIGNATION {get; set;}

public:

property PropertyValue^ FUNC_CABLE_DESIGNATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This field is provided for the entry of text to be later displayed next to the cable or conduit in the schematic, e.g., "OELFLEX-SERVO-FD 4G1.5+2x(2x0.75StD) CP".
