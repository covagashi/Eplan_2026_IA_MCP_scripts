# FUNCTION3D_DESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_DESCRIPTION().html

---

Item description # 36018.

Syntax

**C#**



public PropertyValue FUNCTION3D_DESCRIPTION {get; set;}

public:

property PropertyValue^ FUNCTION3D_DESCRIPTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Contains the item description of a mechanical item. This property is particularly useful for items that do not have a DT, e.g. cable ducts.
