# Pages Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Pages.html

---

Project's property which return array of Pages placed in project. When the project's PagesFilter was set-up, pages matching the filter are returned.

Syntax

**C#**



public Page[] Pages {get;}

public:

property array<Page^>^ Pages {

   array<Page^>^ get();

}


#### Property Value

array of pages. Array's property `Length` gives information about amount of found Pages in Project

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the project is transient. |
