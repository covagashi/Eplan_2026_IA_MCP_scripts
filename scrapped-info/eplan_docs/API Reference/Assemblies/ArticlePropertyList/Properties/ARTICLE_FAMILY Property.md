# ARTICLE_FAMILY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_FAMILY().html

---

Family # 22885.

Syntax

**C#**



public PropertyValue ARTICLE_FAMILY {get; set;}

public:

property PropertyValue^ ARTICLE_FAMILY {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Used to group several cables of the same type. This allows searching for alternatives to a cable in Cable proD (for example for prefabricated cables with the same plugs but different lengths).
