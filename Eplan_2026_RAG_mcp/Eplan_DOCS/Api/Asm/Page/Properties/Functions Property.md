# Functions Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Functions.html

---

Returns all [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s placed on the page. If the filter was set up, returns [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching the filter.

Syntax

**C#**



public Function[] Functions {get;}

public:

property array<Function^>^ Functions {

   array<Function^>^ get();

}


#### Property Value

[Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s on the page.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the page is transient. |
