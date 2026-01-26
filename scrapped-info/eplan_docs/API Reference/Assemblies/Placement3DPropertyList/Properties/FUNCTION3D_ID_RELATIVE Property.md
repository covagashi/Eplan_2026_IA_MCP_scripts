# FUNCTION3D_ID_RELATIVE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_ID_RELATIVE().html

---

Item ID (relative to macro, EEC) # 36035.

Syntax

**C#**



public PropertyValue FUNCTION3D_ID_RELATIVE {get; set;}

public:

property PropertyValue^ FUNCTION3D_ID_RELATIVE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Identifies the individual 3D part placements for a part that consists of several combined 3D part placements. The property is required by the Eplan Engineering Configuration in order to define the items of a macro on which other items are installed.
