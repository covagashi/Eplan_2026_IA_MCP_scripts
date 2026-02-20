# FUNCTION3D_OPENING_HEIGHT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_OPENING_HEIGHT().html

---

Cut-out: Height # 36021.

Syntax

**C#**



public PropertyValue FUNCTION3D_OPENING_HEIGHT {get; set;}

public:

property PropertyValue^ FUNCTION3D_OPENING_HEIGHT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Height of the cut-out. The units are imported from the project settings or converted to mm in case of input in inches.
