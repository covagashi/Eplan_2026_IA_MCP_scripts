# CreateTransient Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Text~CreateTransient(Project,String,Double).html

---

Creates transient and not placed Text object.

Syntax

**C#**



public void CreateTransient( 

   Project oProject,

   string contents,

   double textHeight

)

public:

void CreateTransient( 

   Project^ oProject,

   String^ contents,

   double textHeight

)


#### Parameters

*oProject*
:   [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) the Text will be assign to.

*contents*
:   System.String containing text to display.

*textHeight*
:   Height of the Text.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `oProject` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `contents` is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the Text cannot be created. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the Text has already been created. |
| [Eplan.EplApi.DataModel.IncorrectObjectTypeException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IncorrectObjectTypeException.html) | Thrown when function is invoked with object of higher class. |

Remarks

After creation object is not stored in project database. It can be inserted into database after execution of [Eplan.EplApi.DataModel.Placement.CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~CopyTo(Group).html).
