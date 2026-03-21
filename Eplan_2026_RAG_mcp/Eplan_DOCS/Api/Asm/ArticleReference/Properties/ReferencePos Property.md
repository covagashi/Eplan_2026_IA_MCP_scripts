# ReferencePos Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~ReferencePos.html

---

Returns the index of the ArticleReference reference for the given article if it is referenced by a [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html). This number is useful when reading values of article reference properties (indexed properties on function, e.g. FUNC\_ARTICLE\_COUNT). It is not equal to the 0-based position of element in the table of articles which is returned by Function.Articles/>

Syntax

**C#**



public int ReferencePos {get;}

public:

property int ReferencePos {

   int get();

}


#### Property Value

Index(1-based) of the article reference in the function (if referenced there) or 0.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when index cannot be read. |
