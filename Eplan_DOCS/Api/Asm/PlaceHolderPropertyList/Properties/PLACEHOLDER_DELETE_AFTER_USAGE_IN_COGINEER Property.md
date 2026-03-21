# PLACEHOLDER_DELETE_AFTER_USAGE_IN_COGINEER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic711.html

---

Remove placeholder object after generation with Eplan Cogineer # 19315.

Syntax

**C#**



public PropertyValue PLACEHOLDER_DELETE_AFTER_USAGE_IN_COGINEER {get; set;}

public:

property PropertyValue^ PLACEHOLDER_DELETE_AFTER_USAGE_IN_COGINEER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

If the property is activated, the placeholder object is deleted from the schematic after the generation of the schematic with Eplan Cogineer.
