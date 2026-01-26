# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~Properties.html

---

.NET Property enabling access to P8 properties of the Article object.

Syntax

**C#**



public new ArticlePropertyList Properties {get;}

public:

new property ArticlePropertyList^ Properties {

   ArticlePropertyList^ get();

}


#### Property Value

P8 properties of the Article.

Example

**C#**

```
Article a;//a valid Article

a.Properties[Properties.Article.ARTICLE_NOTE] = "note";

string s = a.Properties[Properties.Article.ARTICLE_SUPPLIER];
```
