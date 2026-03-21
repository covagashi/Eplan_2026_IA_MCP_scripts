# CanHaveArticleData Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~CanHaveArticleData.html

---

Check if the Connection can have [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s.

Syntax

**C#**



public virtual bool CanHaveArticleData {get;}

public:

virtual property bool CanHaveArticleData {

   bool get();

}


#### Property Value

true : Connection can have [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s

false : Connection cannot have [Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the information cannot be retrieved from data model. |
