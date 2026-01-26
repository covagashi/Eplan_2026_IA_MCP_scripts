# InteractionContext

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.InteractionContext.html

---

This class is used to pass information about current state of environment and placements to GED interaction.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)  
      **Eplan.EplApi.EServices.Ged.InteractionContext**

Syntax

**C#**



public class InteractionContext : Eplan.EplApi.Base.Context, Eplan.EplApi.Base.IContext

public ref class InteractionContext : public Eplan.EplApi.Base.Context, Eplan.EplApi.Base.IContext

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [InteractionContext Constructor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.InteractionContext~_ctor().html) | Creates a new InteractionContext object. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Placements](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.InteractionContext~Placements.html) | Placements in this context. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~AddParameter.html) | Adds a parameter to the Context. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [Dispose()](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~Dispose().html) | Destructor for deterministic finalization of InteractionContext object. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [GetContextParameter](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.InteractionContext~GetContextParameter.html) | Overridden. Get the Block of Context Parameters of this Context. |
| Public Method | [GetEContext](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetEContext.html) | For internal use only. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [GetParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetParameter.html) | Gets a parameter from the Context. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [GetParameterCount](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetParameterCount.html) | Gets the count of the Parameters in this context (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [GetParameters](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetParameters.html) | Gets array filled with parameters names from the context. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [GetStrings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetStrings.html) | Gets the array filled with strings from the context. (Additional to the parameters) (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [SetContextParameter](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.InteractionContext~SetContextParameter.html) | Overridden. Sets a block of context parameters (as ContextParameterBlock object). |
| Public Method | [SetEContext](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~SetEContext.html) | For internal use only. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [SetStrings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~SetStrings.html) | Sets the array filled with strings from the context. (Additional to the parameters) (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |


