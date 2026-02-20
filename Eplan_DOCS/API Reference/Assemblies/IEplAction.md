# IEplAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAction.html

---

Interface declaration for an action. When an action is to be registered for an add-in (an assembly) in the system, this interface must be implemented by a class of the add-in.

Syntax

**C#**



[Guid("83FAA39E-2215-3984-982F-29FFB4B3F5F2")]

public interface IEplAction

[Guid("83FAA39E-2215-3984-982F-29FFB4B3F5F2")]

public interface class IEplAction


Remarks

Action names with . are not allowed.

Example

Implementation of a Action in an add-in

**C#**

```
public class NewAction: IEplAction

{	

    public bool Execute(ActionCallingContext ctx)

    {

        // TODO: 

        // Add code

  new Decider().Decide(EnumDecisionType.eOkDecision, "NewAction was invoked!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

        return true;

    }

 public bool OnRegister(ref string Name, ref int Ordinal)

 {

     Name	= "NewAction";

     Ordinal	= 20;

     return true;

 }

 public  void GetActionProperties(ref ActionProperties actionProperties)

 {

     actionProperties.Description= "Description of NewAction";

 }
```

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [Execute](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAction~Execute.html) | Called by the framework when the action is to be performed. |
| Method | [GetActionProperties](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAction~GetActionProperties.html) | Returns descriptive data for the action. For documentation purposes only. |
| Method | [OnRegister](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAction~OnRegister.html) | The action can be registered under a name determined by the action and an overload level. |


