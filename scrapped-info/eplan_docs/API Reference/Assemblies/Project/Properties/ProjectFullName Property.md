# ProjectFullName Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ProjectFullName.html

---

Project's property which return full project name, without an extension.

Syntax

**C#**



public string ProjectFullName {get;}

public:

property String^ ProjectFullName {

   String^ get();

}


#### Property Value

string : project's full name for example "C:\\EPLAN\\PROJECTS\\USER\\EPLAN\_Sample\_Project"

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the project is transient. |
