# ArticleAssemblies Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~ArticleAssemblies.html

---

Returns an array of [Article.Assembly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article+Assembly.html) objects representing parts of an assembly.

Syntax

**C#**



public Article.Assembly[] ArticleAssemblies {get;}

public:

property array<Article.Assembly^>^ ArticleAssemblies {

   array<Article.Assembly^>^ get();

}


Remarks

If this article is not an assembly or it doesn't contain any assembly parts, an empty array is returned.
