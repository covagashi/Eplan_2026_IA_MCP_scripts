# ARTICLE_VARIANT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VARIANT().html

---

Variant # 22024.

Syntax

**C#**



public PropertyValue ARTICLE_VARIANT {get; set;}

public:

property PropertyValue^ ARTICLE_VARIANT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Shows the designation of the variant, up to 3 characters may be entered. A part always has at least one variant. By default, the variant designation "1" is assigned to the first variant of each part.
