# FUNCTION3D_ELEM_ISFIXONPARENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_ELEM_ISFIXONPARENT().html

---

Item is immovably attached to the superior item # 36010.

Syntax

**C#**



public PropertyValue FUNCTION3D_ELEM_ISFIXONPARENT {get; set;}

public:

property PropertyValue^ FUNCTION3D_ELEM_ISFIXONPARENT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is enabled, then the item cannot be moved relative to the superior item. Moving the entire mounting panel by means of the "Move" functionality is still possible. The fixation can be temporarily revoked for individual items by pressing the [Shift] key while moving via Drag & Drop.
