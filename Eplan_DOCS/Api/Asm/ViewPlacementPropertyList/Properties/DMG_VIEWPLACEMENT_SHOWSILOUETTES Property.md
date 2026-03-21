# DMG_VIEWPLACEMENT_SHOWSILOUETTES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_SHOWSILOUETTES().html

---

Model view: Display item silhouettes # 36513.

Syntax

**C#**



public PropertyValue DMG_VIEWPLACEMENT_SHOWSILOUETTES {get; set;}

public:

property PropertyValue^ DMG_VIEWPLACEMENT_SHOWSILOUETTES {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is activated, the basic outlines of extruded items (e.g., mounting rails and wire ducts) and the lateral boundary lines of the 3D object generated from the basic outline will be displayed. Disabling this setting will accelerate the output of complex 2D drilling views, but will impair the quality of the illustration of the items.
