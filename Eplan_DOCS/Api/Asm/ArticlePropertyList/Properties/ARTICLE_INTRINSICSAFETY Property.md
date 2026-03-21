# ARTICLE_INTRINSICSAFETY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_INTRINSICSAFETY().html

---

Intrinsically safe # 22114.

Syntax

**C#**



public PropertyValue ARTICLE_INTRINSICSAFETY {get; set;}

public:

property PropertyValue^ ARTICLE_INTRINSICSAFETY {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Property of a part variant. Shows whether the part is intrinsically safe. In this case it is guaranteed that during operation or in case of a short circuit no spark can occur which could ignite any explosive atmosphere possibly present (gas or liquid).
