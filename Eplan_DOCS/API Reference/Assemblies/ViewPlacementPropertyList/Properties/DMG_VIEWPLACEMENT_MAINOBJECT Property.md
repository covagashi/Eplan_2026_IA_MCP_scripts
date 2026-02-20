# DMG_VIEWPLACEMENT_MAINOBJECT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_MAINOBJECT().html

---

Model view: Basic item # 36509.

Syntax

**C#**



public PropertyValue DMG_VIEWPLACEMENT_MAINOBJECT {get; set;}

public:

property PropertyValue^ DMG_VIEWPLACEMENT_MAINOBJECT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

The basic item is used to specify what is to be displayed in the model view. You can also further restrict the content of the layout space that is displayed. In the case of 2D drilling views and model views, the basic items can also be components of lower item hierarchy levels, e.g. mounting surfaces. In the case of copper unfolds, this is not possible.

If the selected basic items do not contain any graphics, the next-higher item with graphics is added automatically.
