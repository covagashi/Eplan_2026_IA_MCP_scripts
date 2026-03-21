# ActionCallingContext

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext.html

---

This is the ActionCallingContext class used to pass parameters to an action and to receive return values of the action.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)  
      **Eplan.EplApi.ApplicationFramework.ActionCallingContext**  
         [Eplan.EplApi.DataModel.StorableObjectContext](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectContext.html)

Syntax

**C#**



[Guid("B44C4085-E6B8-3622-A1EF-50DF81A26485")]

public class ActionCallingContext : Eplan.EplApi.Base.Context, IActionCallingContext, Eplan.EplApi.Base.IContext

[Guid("B44C4085-E6B8-3622-A1EF-50DF81A26485")]

public ref class ActionCallingContext : public Eplan.EplApi.Base.Context, IActionCallingContext, Eplan.EplApi.Base.IContext


Remarks

Using AddParameter(...) you can add explicitly named parameters to the ActionCallingContext. The action must use this explicit name to reference these parameters. Likewise, values returned by the action can be added. Please mind that an Action may modify the ActionCallingContext during its execution. Sometimes e.g. project IDs are added to the context and are passed to an inner action. Reusing the same ActionCallingContext for another Action call may lead to unexpected results. So in most cases it is advisable to create a new ActionCallingContext for a new Action call.

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ActionCallingContext Constructor](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext~_ctor().html) | Creates an ActionCallingContext |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [SysMessages](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext~SysMessages.html) | Gets system messages |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~AddParameter.html) | Adds a parameter to the Context. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [Dispose()](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~Dispose().html) | Destructor for deterministic finalization of ActionCallingContext object. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [GetAfActionCallingContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext~GetAfActionCallingContext.html) | For internal use only. |
| Public Method | [GetContextParameter](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext~GetContextParameter.html) | Overridden. Get the Block of Context Parameters of this Context. |
| Public Method | [GetEContext](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetEContext.html) | For internal use only. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [GetException](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext~GetException.html) | Get Exception |
| Public Method | [GetParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetParameter.html) | Gets a parameter from the Context. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [GetParameterCount](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetParameterCount.html) | Gets the count of the Parameters in this context (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [GetParameters](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetParameters.html) | Gets array filled with parameters names from the context. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [GetStrings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetStrings.html) | Gets the array filled with strings from the context. (Additional to the parameters) (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [SetAfActionCallingContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext~SetAfActionCallingContext.html) | For internal use only. |
| Public Method | [SetContextParameter](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext~SetContextParameter.html) | Overridden. Sets a block of context parameters (as ContextParameterBlock object). |
| Public Method | [SetEContext](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~SetEContext.html) | For internal use only. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [SetStrings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~SetStrings.html) | Sets the array filled with strings from the context. (Additional to the parameters) (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |


