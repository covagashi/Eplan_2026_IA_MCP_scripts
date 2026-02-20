# FUNCTION3D_ROUTING_SEGMENT_LENGTH_MANUAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_ROUTING_SEGMENT_LENGTH_MANUAL().html

---

Routing path / Curve: Length # 36027.

Syntax

**C#**



public PropertyValue FUNCTION3D_ROUTING_SEGMENT_LENGTH_MANUAL {get; set;}

public:

property PropertyValue^ FUNCTION3D_ROUTING_SEGMENT_LENGTH_MANUAL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Manually entered length of a routing path or curve placed in the layout space. Is used during routing to calculate the precise length of the associated connection.
