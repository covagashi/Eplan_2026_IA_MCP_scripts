# Templates Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PathInfo~Templates.html

---

Returns default Templates directory.

Syntax

**C#**



public string Templates {get;}

public:

property String^ Templates {

   String^ get();

}


#### Property Value

string: default Templates directory

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Exception is thrown when the directory cannot be obtained from settings. |
