# ARTICLE_VARIANT_DESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_VARIANT_DESCRIPTION().html

---

Part variant description # 22887.

Syntax

**C#**



public PropertyValue ARTICLE_VARIANT_DESCRIPTION {get; set;}

public:

property PropertyValue^ ARTICLE_VARIANT_DESCRIPTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Describing text for the variant of a part. Since the variant name is limited to up to three characters, you can use this description to differentiate the variants of a part better.
