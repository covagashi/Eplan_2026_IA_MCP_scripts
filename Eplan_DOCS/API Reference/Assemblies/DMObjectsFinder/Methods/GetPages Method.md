# GetPages Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPages.html

---

Returns [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)s matching given filter.

Syntax

**C#**



public Page[] GetPages( 

   PagesFilter filter

)

public:

array<Page^>^ GetPages( 

   PagesFilter^ filter

)


#### Parameters

*filter*
:   a [PagesFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagesFilter.html), can be `null`

#### Return Value

\* [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)s matching given [PagesFilter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagesFilter.html). \* All [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)s if filter is `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
