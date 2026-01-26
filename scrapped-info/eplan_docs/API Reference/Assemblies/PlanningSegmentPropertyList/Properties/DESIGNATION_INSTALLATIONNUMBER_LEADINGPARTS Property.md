# DESIGNATION_INSTALLATIONNUMBER_LEADINGPARTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic782.html

---

Higher-level function number (single component) # 1728.

Syntax

**C#**



public PropertyValue DESIGNATION_INSTALLATIONNUMBER_PART {get; set;}

public:

property PropertyValue^ DESIGNATION_INSTALLATIONNUMBER_PART {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Part of the higher-level function number that is entered at this planning object. The entire higher-level function number for a planning object consists in this case of the own individual part and all the parts of the superior structure segments and planning objects.
