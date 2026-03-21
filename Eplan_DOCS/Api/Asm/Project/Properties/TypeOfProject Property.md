# TypeOfProject Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~TypeOfProject.html

---

Type of project To change this property project will be reopened temporarily in exclusive mode. If project cannot be reopened in exclusive mode BaseException will be thrown.

Syntax

**C#**



public Project.ProjectType TypeOfProject {get; set;}

public:

property Project.ProjectType TypeOfProject {

   Project.ProjectType get();

   void set (    Project.ProjectType value);

}


#### Property Value

Project type.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if project cannot be opened in exclusive mode. |
| [SettingValueFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SettingValueFailedException.html) | Thrown when new value wasn't assigned to property after set. |
