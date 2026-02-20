# FUNC_CODE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~FUNC_CODE().html

---

DT: Identifier # 20013.

Syntax

**C#**



public PropertyValue FUNC_CODE {get; set;}

public:

property PropertyValue^ FUNC_CODE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

By default, the identifier letter assigned to the function definition is adopted, but this can be overwritten.

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.
