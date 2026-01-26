# DMG_VIEWPLACEMENT_DISPLAY_FREE_ROUTED_CABLES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic716.html

---

Model view: Display freely routed cables # 36515.

Syntax

**C#**



public PropertyValue DMG_VIEWPLACEMENT_DISPLAY_FREE_ROUTED_CABLES {get; set;}

public:

property PropertyValue^ DMG_VIEWPLACEMENT_DISPLAY_FREE_ROUTED_CABLES {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is activated, freely routed cables are also displayed in the model view. If the property is deactivated, freely routed cables are not displayed.
