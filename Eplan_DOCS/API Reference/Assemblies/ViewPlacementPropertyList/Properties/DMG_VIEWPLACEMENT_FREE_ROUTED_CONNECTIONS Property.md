# DMG_VIEWPLACEMENT_FREE_ROUTED_CONNECTIONS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic718.html

---

Model view: Display freely routed wires # 36516.

Syntax

**C#**



public PropertyValue DMG_VIEWPLACEMENT_FREE_ROUTED_CONNECTIONS {get; set;}

public:

property PropertyValue^ DMG_VIEWPLACEMENT_FREE_ROUTED_CONNECTIONS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is activated, freely routed cable connections / wires are also displayed in the model view. If the property is deactivated, freely routed cable connections / wires are not displayed.
