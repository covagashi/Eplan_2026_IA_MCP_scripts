# FCTDEFLIB_LASTMODIFICATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic727.html

---

Modification date # 15501.

Syntax

**C#**



public PropertyValue FCTDEFLIB_LASTMODIFICATIONDATE {get; set;}

public:

property PropertyValue^ FCTDEFLIB_LASTMODIFICATIONDATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Date of last changes to the function definition library. Since function definition libraries cannot be subsequently changed, only generated, this also reflects the creation date. The time is output in the local time of the user in accordance with the set time zone.
