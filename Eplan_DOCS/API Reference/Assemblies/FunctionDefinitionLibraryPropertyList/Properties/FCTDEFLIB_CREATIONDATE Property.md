# FCTDEFLIB_CREATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic726.html

---

Creation date # 15504.

Syntax

**C#**



public PropertyValue FCTDEFLIB_CREATIONDATE {get; set;}

public:

property PropertyValue^ FCTDEFLIB_CREATIONDATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Creation date of the function definition library. The time is output in the local time of the user in accordance with the set time zone.
