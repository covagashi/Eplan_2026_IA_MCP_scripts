# FUNCTION3D_OPENING_DIAMETER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_OPENING_DIAMETER().html

---

Cut-out: Diameter of the hole # 36006.

Syntax

**C#**



public PropertyValue FUNCTION3D_OPENING_DIAMETER {get; set;}

public:

property PropertyValue^ FUNCTION3D_OPENING_DIAMETER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Drill hole diameter. The units are imported from the project settings or converted to mm in case of input in inches.
