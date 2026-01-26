# ImageDirectory Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ImageDirectory.html

---

Project's property which return full project images' directory name.

Syntax

**C#**



public string ImageDirectory {get;}

public:

property String^ ImageDirectory {

   String^ get();

}


#### Property Value

string : project images' directory path for example "C:EPLAN\\PROJECTS\\EPLAN\_Sample\_Project.edb\\Images"

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the project is transient. |
