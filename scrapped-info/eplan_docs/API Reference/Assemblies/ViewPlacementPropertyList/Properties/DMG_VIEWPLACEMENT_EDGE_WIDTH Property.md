# DMG_VIEWPLACEMENT_EDGE_WIDTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_EDGE_WIDTH().html

---

Model view: Edge width # 36524.

Syntax

**C#**



public PropertyValue DMG_VIEWPLACEMENT_EDGE_WIDTH {get; set;}

public:

property PropertyValue^ DMG_VIEWPLACEMENT_EDGE_WIDTH {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

With this property you can set the width of the edge lines in the model view, 2D drilling view and copper unfold to a fixed value, for example 0.5 mm. During zooming and at scale changes the line width is adapted correspondingly. During PDF export the edge lines are output with the specified width. If no value is entered, the line thickness amounts to one pixel.
