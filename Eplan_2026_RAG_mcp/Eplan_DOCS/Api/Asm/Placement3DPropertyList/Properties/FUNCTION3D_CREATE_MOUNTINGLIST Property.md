# FUNCTION3D_CREATE_MOUNTINGLIST Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_CREATE_MOUNTINGLIST().html

---

Output in mounting list # 36032.

Syntax

**C#**



public PropertyValue FUNCTION3D_CREATE_MOUNTINGLIST {get; set;}

public:

property PropertyValue^ FUNCTION3D_CREATE_MOUNTINGLIST {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is activated for a 3D part placement, the 3D part placement is output when mounting lists are generated.
