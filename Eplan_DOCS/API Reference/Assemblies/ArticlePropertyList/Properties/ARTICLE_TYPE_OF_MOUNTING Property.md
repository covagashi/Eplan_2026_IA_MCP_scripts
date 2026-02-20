# ARTICLE_TYPE_OF_MOUNTING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TYPE_OF_MOUNTING().html

---

Mounting type # 26187.

Syntax

**C#**



public PropertyValue ARTICLE_TYPE_OF_MOUNTING {get; set;}

public:

property PropertyValue^ ARTICLE_TYPE_OF_MOUNTING {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Specifies the specific method or technology with which an item is installed or fastened at a foreseen position. The following values are possible:

0 = Undefined

1 = Roof mounted

2 = Free-standing

3 = Integrated

4 = Wall-mounted
