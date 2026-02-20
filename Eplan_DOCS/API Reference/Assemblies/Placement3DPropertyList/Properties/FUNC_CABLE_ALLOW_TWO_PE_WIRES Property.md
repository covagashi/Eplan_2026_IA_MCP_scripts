# FUNC_CABLE_ALLOW_TWO_PE_WIRES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_CABLE_ALLOW_TWO_PE_WIRES().html

---

Allow multiple PE conductors # 20062.

Syntax

**C#**



public PropertyValue FUNC_CABLE_ALLOW_TWO_PE_WIRES {get; set;}

public:

property PropertyValue^ FUNC_CABLE_ALLOW_TWO_PE_WIRES {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Suppresses the message "Several PE conductors intersected" in the project review.
