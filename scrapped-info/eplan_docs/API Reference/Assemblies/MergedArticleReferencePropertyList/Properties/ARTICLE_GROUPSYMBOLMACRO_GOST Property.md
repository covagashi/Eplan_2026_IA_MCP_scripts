# ARTICLE_GROUPSYMBOLMACRO_GOST Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_GROUPSYMBOLMACRO_GOST().html

---

Schematic macro: GOST # 22874.

Syntax

**C#**



public PropertyValue ARTICLE_GROUPSYMBOLMACRO_GOST {get; set;}

public:

property PropertyValue^ ARTICLE_GROUPSYMBOLMACRO_GOST {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

2D macro that is placed preferentially on schematic pages if the "GOST" standard is specified as the preferred standard in the project settings. This macro is only used if no company standard is specified in the project settings or if no corresponding schematic macro for the company standard is stored at the part.
