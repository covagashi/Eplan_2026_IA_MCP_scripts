# DESIGNATION_SUBLOCATION7 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~DESIGNATION_SUBLOCATION7().html

---

Location designation (sub-identifier 7) # 1207.

Syntax

**C#**



public PropertyValue DESIGNATION_SUBLOCATION7 {get; set;}

public:

property PropertyValue^ DESIGNATION_SUBLOCATION7 {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.
