# DESIGNATION_INSTALLATIONNUMBER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList~DESIGNATION_INSTALLATIONNUMBER().html

---

Higher-level function number (main identifier) # 1700.

Syntax

**C#**



public PropertyValue DESIGNATION_INSTALLATIONNUMBER {get; set;}

public:

property PropertyValue^ DESIGNATION_INSTALLATIONNUMBER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

The first (and in this case only) hierarchy level of the higher-level function number. Is required for fluid power.

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.
