# ArticleReferences Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ArticleReferences.html

---

Returns [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s that are referenced by Project.

Syntax

**C#**



public virtual ArticleReference[] ArticleReferences {get;}

public:

virtual property array<ArticleReference^>^ ArticleReferences {

   array<ArticleReference^>^ get();

}


#### Property Value

ArticleReferences related with the Project

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal query for Projects throws exception |
