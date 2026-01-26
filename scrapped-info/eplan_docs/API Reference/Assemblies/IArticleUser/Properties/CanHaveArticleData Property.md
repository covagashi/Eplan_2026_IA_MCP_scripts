# CanHaveArticleData Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IArticleUser~CanHaveArticleData.html

---

Check if the IArticleUser can have [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s.

Syntax

**C#**



bool CanHaveArticleData {get;}

property bool CanHaveArticleData {

   bool get();

}


#### Property Value

true : IArticleUser can have [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s

false : IArticleUser cannot have [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the information cannot be retrieved from data model. |
