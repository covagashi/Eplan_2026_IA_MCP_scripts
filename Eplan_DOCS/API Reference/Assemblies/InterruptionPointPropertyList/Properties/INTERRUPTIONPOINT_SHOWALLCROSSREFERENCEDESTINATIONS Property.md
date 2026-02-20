# INTERRUPTIONPOINT_SHOWALLCROSSREFERENCEDESTINATIONS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic270.html

---

Display of all counter targets # 24021.

Syntax

**C#**



public PropertyValue INTERRUPTIONPOINT_SHOWALLCROSSREFERENCEDESTINATIONS {get; set;}

public:

property PropertyValue^ INTERRUPTIONPOINT_SHOWALLCROSSREFERENCEDESTINATIONS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this setting is switched on at an interruption point, then the "Cross-reference (configurable)" (ID 24300) and / or the "Counter target in cross-reference" (ID 24351) properties show all counter targets.

If this property is activated and the project setting "Display target at pair cross-references" is deactivated, the setting trumps at the interruption point, and all targets are displayed.

If this property is deactivated and the project setting "Display target at pair cross-references" is activated, the first target is displayed.
