# GetPagesWithFilterScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DMObjectsFinder~GetPagesWithFilterScheme.html

---

\Returns [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html)s matching given filter from pages-navigator(user settings) or if such doesn't exist filter with use of project settings is created. There can be different results when using page filter now and in 1.9 version. For further information please look in P8 help chapter concerning page filter.

Syntax

**C#**



public Page[] GetPagesWithFilterScheme( 

   string strFilterScheme

)

public:

array<Page^>^ GetPagesWithFilterScheme( 

   String^ strFilterScheme

)


#### Parameters

*strFilterScheme*
:   Scheme\-name of filter pages\-navigator

#### Return Value

\* If scheme-name is empty, the current filter-scheme will be used. \* If scheme-name is null, the method returns elements that are visible if no filter scheme is used in a GUI navigator.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if internally used query throws exception. |
| [System.ArgumentException](#) | Thrown if filter scheme does not exist. |
| [System.ArgumentNullException](#) | Thrown if strFilterScheme is set to null. |

Remarks

If you have an old page filter scheme (List with preselection) and a new filter scheme wit the same name, this method will use the new one. In case of an old filter scheme, the scheme is always the one for the pre-filter.
