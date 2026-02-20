# IContext

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.IContext.html

---

IContext is an abstract interface for Context classes.

Syntax

**C#**



public interface IContext

public interface class IContext


Remarks

Context classes are used to pass information about the current state of the environment as well as generic parameters to objects that can be registered such as actions, dialogs, etc.

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [AddParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.IContext~AddParameter.html) | Adds a parameter to the Context. |
| Method | [GetParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.IContext~GetParameter.html) | Gets a parameter from the Context. |
| Method | [GetParameterCount](Eplan.EplApi.Baseu~Eplan.EplApi.Base.IContext~GetParameterCount.html) | Gets the count of the Parameters in this context |
| Method | [GetParameters](Eplan.EplApi.Baseu~Eplan.EplApi.Base.IContext~GetParameters.html) | Gets array filled with parameters names from the context. |
| Method | [GetStrings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.IContext~GetStrings.html) | Gets array filled with strings from the context. |
| Method | [SetStrings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.IContext~SetStrings.html) | Sets the array filled with strings from the context. (Additional to the parameters) |


