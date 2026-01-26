# CanHaveArticleData Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~CanHaveArticleData.html

---

Check if the Function can have [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s.

Syntax

**C#**



public virtual bool CanHaveArticleData {get;}

public:

virtual property bool CanHaveArticleData {

   bool get();

}


#### Property Value

true : Function can have [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s

false : Function cannot have [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the information cannot be retrieved from data model. |

Remarks

Please mind that Functions of category ArticlePlacement can have only 1 ArticleReference object.
