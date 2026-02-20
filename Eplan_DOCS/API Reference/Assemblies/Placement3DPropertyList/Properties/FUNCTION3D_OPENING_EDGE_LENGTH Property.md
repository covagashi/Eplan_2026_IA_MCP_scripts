# FUNCTION3D_OPENING_EDGE_LENGTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_OPENING_EDGE_LENGTH().html

---

Cut-out: Edge length # 36024.

Syntax

**C#**



public PropertyValue FUNCTION3D_OPENING_EDGE_LENGTH {get; set;}

public:

property PropertyValue^ FUNCTION3D_OPENING_EDGE_LENGTH {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Edge length of the cut-out. The units are imported from the project settings or converted to mm in case of input in inches.
