# ProjectLinkFilePath Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ProjectLinkFilePath.html

---

Project's property which return full project-link file name.

Syntax

**C#**



public string ProjectLinkFilePath {get;}

public:

property String^ ProjectLinkFilePath {

   String^ get();

}


#### Property Value

string : project's link file path, for example "C:\EPLAN\PROJECTS\EPLAN\_Sample\_Project.elk".

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the project is transient. |
