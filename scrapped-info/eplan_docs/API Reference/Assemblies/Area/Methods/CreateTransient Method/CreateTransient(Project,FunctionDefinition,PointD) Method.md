# CreateTransient(Project,FunctionDefinition,PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Area~CreateTransient(Project,FunctionDefinition,PointD).html

---

Creates transient and not placed Area object.

Syntax

**C#**



public void CreateTransient( 

   Project oProject,

   FunctionDefinition oFunctionDefinition,

   PointD oSize

)

public:

void CreateTransient( 

   Project^ oProject,

   FunctionDefinition^ oFunctionDefinition,

   PointD oSize

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*oFunctionDefinition*
:   [Eplan.EplApi.DataModel.FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) which determins type of area. Can't be null.

*oSize*
:   Point object which represents height and width of Area object.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.WrongCategoryException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.WrongCategoryException.html) | Thrown when function definitions category is incorrect. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the Area cannot be created. |

Remarks

List of possible function definitions that can be created as Area object is restricted into this:

- Area definition
- Wiring cut-out
- Routing range
