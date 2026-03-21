# FUNCTION3D_PARENT_OBJECTID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_PARENT_OBJECTID().html

---

Superior mounting surface # 36033.

Syntax

**C#**



public PropertyValue FUNCTION3D_PARENT_OBJECTID {get; set;}

public:

property PropertyValue^ FUNCTION3D_PARENT_OBJECTID {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Specifies the mounting surface on which the 3D part placement has been placed. The property is used in filters to filter for 3D part placements that have been installed on other 3D part placements.
