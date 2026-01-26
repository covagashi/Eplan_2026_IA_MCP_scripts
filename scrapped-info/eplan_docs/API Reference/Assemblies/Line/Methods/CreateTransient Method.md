# CreateTransient Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Line~CreateTransient.html

---

Creates transient and not placed Line object.

Syntax

**C#**



public override void CreateTransient( 

   Project project

)

public:

void CreateTransient( 

   Project^ project

) override


#### Parameters

*project*
:   [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) the Line will be assign to.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `project` is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the Line cannot be created. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Line has already been created. |

Remarks

After creation object is not stored in project database. It can be inserted into database after execution of [Eplan.EplApi.DataModel.Placement.CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~CopyTo(Group).html).
