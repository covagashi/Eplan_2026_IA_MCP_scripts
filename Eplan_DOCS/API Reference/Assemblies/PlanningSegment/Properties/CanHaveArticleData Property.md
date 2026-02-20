# CanHaveArticleData Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~CanHaveArticleData.html

---

Check if the PlanningSegment can have [Eplan.EplApi.DataModel.Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s.

Syntax

**C#**



public virtual bool CanHaveArticleData {get;}

public:

virtual property bool CanHaveArticleData {

   bool get();

}


#### Property Value

true : PlanningSegment can have [Eplan.EplApi.DataModel.Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s

false : PlanningSegment cannot have [Eplan.EplApi.DataModel.Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html)s

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the information cannot be retrieved from data model. |
