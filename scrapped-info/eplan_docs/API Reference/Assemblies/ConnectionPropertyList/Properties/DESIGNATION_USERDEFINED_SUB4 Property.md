# DESIGNATION_USERDEFINED_SUB4 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_USERDEFINED_SUB4().html

---

User-defined structure (sub-identifier 4) # 1604.

Syntax

**C#**



public PropertyValue DESIGNATION_USERDEFINED_SUB4 {get; set;}

public:

property PropertyValue^ DESIGNATION_USERDEFINED_SUB4 {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the sublevel 4 of the user-defined structure.

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.
