# StorableObjectContext

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectContext.html

---

This is a context with a Storable Object or a list of storable objects.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)  
      [Eplan.EplApi.ApplicationFramework.ActionCallingContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext.html)  
         **Eplan.EplApi.DataModel.StorableObjectContext**

Syntax

**C#**



public class StorableObjectContext : Eplan.EplApi.ApplicationFramework.ActionCallingContext, Eplan.EplApi.ApplicationFramework.IActionCallingContext, Eplan.EplApi.Base.IContext

public ref class StorableObjectContext : public Eplan.EplApi.ApplicationFramework.ActionCallingContext, Eplan.EplApi.ApplicationFramework.IActionCallingContext, Eplan.EplApi.Base.IContext

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [StorableObjectContext Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectContext~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectContext~StorableObject.html) | Set or get a Storable Object for this context |
| Public Property | [StorableObjectList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectContext~StorableObjectList.html) | Set or get a Storable Object List for this context (additional to the single Storable Object) |
| Public Property | [SysMessages](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext~SysMessages.html) | Gets system messages (Inherited from [Eplan.EplApi.ApplicationFramework.ActionCallingContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~AddParameter.html) | Adds a parameter to the Context. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [Dispose()](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~Dispose().html) | Destructor for deterministic finalization of StorableObjectContext object. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [GetAfActionCallingContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext~GetAfActionCallingContext.html) | For internal use only. (Inherited from [Eplan.EplApi.ApplicationFramework.ActionCallingContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext.html)) |
| Public Method | [GetContextParameter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectContext~GetContextParameter.html) | Overridden. Get the Block of Context Parameters of this Context. |
| Public Method | [GetDMBaseHandleContext](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectContext~GetDMBaseHandleContext.html) | For internal use only. |
| Public Method | [GetEContext](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetEContext.html) | For internal use only. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [GetException](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext~GetException.html) | Get Exception (Inherited from [Eplan.EplApi.ApplicationFramework.ActionCallingContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext.html)) |
| Public Method | [GetParameter](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetParameter.html) | Gets a parameter from the Context. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [GetParameterCount](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetParameterCount.html) | Gets the count of the Parameters in this context (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [GetParameters](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetParameters.html) | Gets array filled with parameters names from the context. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [GetStrings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetStrings.html) | Gets the array filled with strings from the context. (Additional to the parameters) (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [SetAfActionCallingContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext~SetAfActionCallingContext.html) | For internal use only. (Inherited from [Eplan.EplApi.ApplicationFramework.ActionCallingContext](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.ActionCallingContext.html)) |
| Public Method | [SetContextParameter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectContext~SetContextParameter.html) | Overridden. Sets a block of context parameters (as ContextParameterBlock object). |
| Public Method | [SetDMBaseHandleContext](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectContext~SetDMBaseHandleContext.html) | For internal use only. |
| Public Method | [SetEContext](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~SetEContext.html) | For internal use only. (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |
| Public Method | [SetStrings](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~SetStrings.html) | Sets the array filled with strings from the context. (Additional to the parameters) (Inherited from [Eplan.EplApi.Base.Context](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context.html)) |


