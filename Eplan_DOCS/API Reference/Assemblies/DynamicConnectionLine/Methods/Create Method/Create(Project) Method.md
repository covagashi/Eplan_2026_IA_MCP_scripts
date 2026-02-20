# Create(Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DynamicConnectionLine~Create(Project).html

---

Creates DynamicConnectionLine object.

Syntax

**C#**



public void Create( 

   Project proj

)

public:

void Create( 

   Project^ proj

)


#### Parameters

*proj*
:   [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) inside which the object will be located.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when a DynamicConnectionLine cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
