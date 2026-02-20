# DMG_VIEWPLACEMENT_TEXTDIRECTION_LIKE_IN_3D Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic722.html

---

Model view: Do not automatically rotate texts from layout space # 36525.

Syntax

**C#**



public PropertyValue DMG_VIEWPLACEMENT_TEXTDIRECTION_LIKE_IN_3D {get; set;}

public:

property PropertyValue^ DMG_VIEWPLACEMENT_TEXTDIRECTION_LIKE_IN_3D {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If the property is activated, the property texts are aligned according to the definition in the layout space and the rotation of the view. If this property is deactivated, property texts are generated readable norm-compliant from below or the left in the model view. The setting only affects property texts that are transferred from the layout space.
