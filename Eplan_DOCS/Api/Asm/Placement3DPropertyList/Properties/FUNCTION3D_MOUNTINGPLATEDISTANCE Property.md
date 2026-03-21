# FUNCTION3D_MOUNTINGPLATEDISTANCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_MOUNTINGPLATEDISTANCE().html

---

Distance to mounting surface # 36017.

Syntax

**C#**



public PropertyValue FUNCTION3D_MOUNTINGPLATEDISTANCE {get; set;}

public:

property PropertyValue^ FUNCTION3D_MOUNTINGPLATEDISTANCE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

If an offset was entered during the placement of a part, this property will display the distance of the part placement from the mounting surface.
