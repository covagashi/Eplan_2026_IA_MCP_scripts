# Context

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html

---

The Context classes are used to pass information about the current state of the environment as well as generic parameters to objects that can be registered such as actions, dialogs, etc.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.Context**  
      [Eplan.EplApi.ApplicationFramework.ActionCallingContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext.html)  
      [Eplan.EplApi.EServices.Ged.InteractionContext](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.InteractionContext.html)

Syntax

**C#**



public class Context : IContext

public ref class Context : public IContext

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Context Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~_ctor.html) | Overloaded. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~AddParameter.html) | Adds a parameter to the Context. |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~Dispose().html) | Destructor for deterministic finalization of Context object. |
| Public Method | [GetContextParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetContextParameter.html) | Get the Block of Context Parameters of this Context. |
| Public Method | [GetEContext](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetEContext.html) | For internal use only. |
| Public Method | [GetParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetParameter.html) | Gets a parameter from the Context. |
| Public Method | [GetParameterCount](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetParameterCount.html) | Gets the count of the Parameters in this context |
| Public Method | [GetParameters](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetParameters.html) | Gets array filled with parameters names from the context. |
| Public Method | [GetStrings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetStrings.html) | Gets the array filled with strings from the context. (Additional to the parameters) |
| Public Method | [SetContextParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~SetContextParameter.html) | Sets a block of context parameters (as ContextParameterBlock object). |
| Public Method | [SetEContext](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~SetEContext.html) | For internal use only. |
| Public Method | [SetStrings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~SetStrings.html) | Sets the array filled with strings from the context. (Additional to the parameters) |


