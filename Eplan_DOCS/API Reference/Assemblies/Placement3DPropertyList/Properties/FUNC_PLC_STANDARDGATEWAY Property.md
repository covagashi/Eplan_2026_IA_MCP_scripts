# FUNC_PLC_STANDARDGATEWAY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLC_STANDARDGATEWAY().html

---

Standard gateway # 20613.

Syntax

**C#**



public PropertyValue FUNC_PLC_STANDARDGATEWAY {get; set;}

public:

property PropertyValue^ FUNC_PLC_STANDARDGATEWAY {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Packets that cannot be directly forwarded within a LAN are sent to the standard gateway (e.g. a router).
