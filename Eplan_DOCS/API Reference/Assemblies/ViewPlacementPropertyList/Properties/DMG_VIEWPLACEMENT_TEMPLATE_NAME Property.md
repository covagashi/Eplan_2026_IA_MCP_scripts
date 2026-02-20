# DMG_VIEWPLACEMENT_TEMPLATE_NAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_TEMPLATE_NAME().html

---

Model view: Name of the report template # 36512.

Syntax

**C#**



public PropertyValue DMG_VIEWPLACEMENT_TEMPLATE_NAME {get; set;}

public:

property PropertyValue^ DMG_VIEWPLACEMENT_TEMPLATE_NAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Name of the used report template for the automatic generation of model views, copper unfolds or 2D drilling views. At a renewed report this report template is used again.
