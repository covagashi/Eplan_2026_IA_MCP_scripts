# PAGE_SUBCOUNTER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_SUBCOUNTER().html

---

Page subcounter # 11013.

Syntax

**C#**



public PropertyValue PAGE_SUBCOUNTER {get; set;}

public:

property PropertyValue^ PAGE_SUBCOUNTER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

This property can be used in forms (for example for the Table of contents), but is not designed for use in filters.

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.
