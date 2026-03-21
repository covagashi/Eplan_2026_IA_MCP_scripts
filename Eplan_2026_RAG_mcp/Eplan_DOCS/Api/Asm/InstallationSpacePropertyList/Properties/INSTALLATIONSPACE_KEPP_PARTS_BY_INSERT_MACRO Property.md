# INSTALLATIONSPACE_KEPP_PARTS_BY_INSERT_MACRO Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic479.html

---

Keep parts at placement # 36457.

Syntax

**C#**



public PropertyValue INSTALLATIONSPACE_KEPP_PARTS_BY_INSERT_MACRO {get; set;}

public:

property PropertyValue^ INSTALLATIONSPACE_KEPP_PARTS_BY_INSERT_MACRO {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is evaluated during the generation of macros from a macro project, and assigned to the generated macro variants. If the property is activated, the macro stored on the part is placed unchanged when a device is inserted. The part number of the device is not used in this case, but instead the part numbers entered in the macro are retained.

If the property is deactivated, the part number of the device is used, and carried over to the main function of the macro.
