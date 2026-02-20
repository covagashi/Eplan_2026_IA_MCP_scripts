# Images Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PathInfo~Images.html

---

Returns default Images directory.

Syntax

**C#**



public string Images {get;}

public:

property String^ Images {

   String^ get();

}


#### Property Value

string : default Images directory

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Exception is thrown when the directory cannot be obtained from settings. |
