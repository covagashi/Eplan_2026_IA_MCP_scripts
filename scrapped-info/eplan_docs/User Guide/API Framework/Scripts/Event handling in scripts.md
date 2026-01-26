# Event handling in scripts

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Script_EventHandling.html

---

You can write a script to react on EPLAN events. To do this, you must declare at least one function of the script as an event handler using the  [DeclareEventHandler()]  attribute and load the script.

It is even possible to handle event parameters. However, you need to know the event parameters in advance.

The following two examples show scripts that respond to events when loaded.

The script in the first example reacts to the  onMainStart  event. The function  MyEventHandlerFunction  in the class  SimpleEventHandler  is registered as event handler for the  onMainStart  event. When this event is raised in EPLAN, the function is called.

The second example shows an event handler script that catches any  onActionStart.String  event. There is an event parameter for the name of the action.

**C#**
```csharp
public class SimpleEventHandler

{

    [DeclareEventHandler("onMainStart")]

     public void MyEventHandlerFunction()

     {

           new Decider().Decide(EnumDecisionType.eOkDecision, "MyEventHandlerFunction was called!","SimpleEventHandler", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

           return;

     }

} 

public class SimpleEventHandler

{

    [DeclareEventHandler("onActionStart.String.*")]

    public long MyEventHandlerFunction2(IEventParameter iEventParameter)

    {

        try

        {

            EventParameterString oEventParameterString= new EventParameterString(iEventParameter);

            String strActionName= oEventParameterString.String;

            new Decider().Decide(EnumDecisionType.eOkDecision, "Action " + strActionName + " was started!","MyEventHandler", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

        }

        catch (System.InvalidCastException exc)

        {

            String strExc= exc.Message;

            new Decider().Decide(EnumDecisionType.eOkDecision, "Parameter error: " + strExc, "MyEventHandler", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

        }

        return 0;

    }

}

Public Class SimpleEventHandler

   <DeclareEventHandler("onMainStart")>  _

      dec.Decide(EnumDecisionType.eOkDecision, "MyEventHandlerFunction was called!", "SimpleEventHandler", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)

Public Class SimpleEventHandler

   <DeclareEventHandler("onActionStart.String.*")>  _

   Public Function MyEventHandlerFunction2(iEventParameter As IEventParameter) As Long

      Try

         dec.Decide(EnumDecisionType.eOkDecision, "Action " + strActionName + " was started!", "MyEventHandler", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)

         dec.Decide(EnumDecisionType.eOkDecision, "Parameter error: " + strExc, "MyEventHandler", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)

      Return 0
```
