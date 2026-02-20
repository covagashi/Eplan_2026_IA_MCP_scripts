# FUNCTION3D_DESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_DESIGNATION().html

---

Item designation # 36000.

Syntax

**C#**



public PropertyValue FUNCTION3D_DESIGNATION {get; set;}

public:

property PropertyValue^ FUNCTION3D_DESIGNATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Contains the item designation of a mechanical item. This property is particularly useful for items that do not have a DT, e.g. cable ducts.
