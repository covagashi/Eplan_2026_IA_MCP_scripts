# DESIGNATION_PLACEOFINSTALLATION_LEADINGPARTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic786.html

---

Installation site (single component) # 1428.

Syntax

**C#**



public PropertyValue DESIGNATION_PLACEOFINSTALLATION_PART {get; set;}

public:

property PropertyValue^ DESIGNATION_PLACEOFINSTALLATION_PART {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Part of the installation site that is entered at this planning object. The entire installation site for a planning object consists in this case of the own individual part and all the parts of the superior structure segments and planning objects.
