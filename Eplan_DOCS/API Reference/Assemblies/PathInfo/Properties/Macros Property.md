# Macros Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PathInfo~Macros.html

---

Returns default Macros directory.

Syntax

**C#**



public string Macros {get;}

public:

property String^ Macros {

   String^ get();

}


#### Property Value

string: default Macros directory

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Exception is thrown when the directory cannot be obtained from settings. |
