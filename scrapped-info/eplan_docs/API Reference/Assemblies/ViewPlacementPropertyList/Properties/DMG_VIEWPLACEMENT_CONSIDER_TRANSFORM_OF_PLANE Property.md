# DMG_VIEWPLACEMENT_CONSIDER_TRANSFORM_OF_PLANE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic715.html

---

Model view: Apply viewpoint to mounting surface # 36508.

Syntax

**C#**



public PropertyValue DMG_VIEWPLACEMENT_CONSIDER_TRANSFORM_OF_PLANE {get; set;}

public:

property PropertyValue^ DMG_VIEWPLACEMENT_CONSIDER_TRANSFORM_OF_PLANE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is activated, the viewpoint of the model view refers to the first mounting surface of the basic items.
