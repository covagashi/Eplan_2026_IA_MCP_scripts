# FUNCTION3D_OPENING_WIDTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_OPENING_WIDTH().html

---

Cut-out: Width # 36020.

Syntax

**C#**



public PropertyValue FUNCTION3D_OPENING_WIDTH {get; set;}

public:

property PropertyValue^ FUNCTION3D_OPENING_WIDTH {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Width of the cut-out. The units are imported from the project settings or converted to mm in case of input in inches.
