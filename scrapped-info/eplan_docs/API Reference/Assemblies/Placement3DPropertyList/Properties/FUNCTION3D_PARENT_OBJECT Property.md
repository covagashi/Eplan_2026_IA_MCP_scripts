# FUNCTION3D_PARENT_OBJECT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_PARENT_OBJECT().html

---

Superior device # 36040.

Syntax

**C#**



public PropertyValue FUNCTION3D_PARENT_OBJECT {get; set;}

public:

property PropertyValue^ FUNCTION3D_PARENT_OBJECT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

The property supplies the directly superior device as the value. The following property values are combined: Full item designation, full DT, legend item.
