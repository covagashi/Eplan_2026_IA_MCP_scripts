# ProjectName Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ProjectName.html

---

Project's property which return Name of Project - project name only without path.

Syntax

**C#**



public string ProjectName {get; set;}

public:

property String^ ProjectName {

   String^ get();

   void set (    String^ value);

}


#### Property Value

project's name, for example "EPLAN\_Sample\_Project"

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the project is transient. |
| [System.ArgumentException](#) | Thrown when setting the name that starts or ends with space character. |
