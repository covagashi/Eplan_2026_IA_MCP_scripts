# Calling actions

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/CallingActions.html

---

All ribbon buttons in P8 are linked to an action. This means that when a ribbon button is called, the corresponding action is executed. In order to execute an action via Eplan API, you have to create an  Action  object and execute the action with the  Execute  method.

In order to create an  Action  object, you need to know the action by its name. You have to create a new  ActionManager  object and call the  FindAction  function, which takes the name of the action as parameter.

To pass and evaluate action parameters, you need the  ActionCallingContext  class:

**C#**
```csharp
String strAction = "TestAction";

ActionManager oAMnr= new ActionManager();

Action oAction= oAMnr.FindAction(strAction);

if (oAction != null)

{

    ActionCallingContext ctx = new ActionCallingContext();

    bool bRet=oAction.Execute(ctx);

    if (bRet)

    {               

    new Decider().Decide(EnumDecisionType.eOkDecision, "The Action " + strAction + " ended successfully!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

    }

    else

    {

    new Decider().Decide(EnumDecisionType.eOkDecision, "The Action " + strAction + " ended with errors!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

    }

}

      dec.Decide(EnumDecisionType.eOkDecision, "The Action " + strAction + " ended successfully!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)              

   Else

      dec.Decide(EnumDecisionType.eOkDecision, "The Action " + strAction + " ended with errors!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)
```

To find out which action is linked to which ribbon button, you can evaluate the  onActionStart.String.\*  event. Alternatively, after clicking the ribbon button, press [Ctrl] + [VK\_OEM\_5] to show the Diagnostics Dialog. [VK\_OEM\_5] corresponds to the [^] key on a German keyboard or to the [\] on a United States 101 keyboard.

For a list of automatic actions, refer to the topic "[Automatic Actions](AutomaticActions.html)".

**Important:**

Please mind that an action may modify the  ActionCallingContext  during its execution. For example, sometimes project IDs are added to the context and are passed to an inner action. Reusing the same  ActionCallingContext  for another action call may lead to unexpected results. So in most cases it is advisable to create a new  ActionCallingContext  for a new action call.

### Command line call

To extend the Eplan command line with new commands and parameters, you need to implement an action. The action can have its own parameters and can call other API functions.

In this way an action is executed just after starting Eplan, for example:

EPLAN.EXE /Variant:"Electric P8" /NoLoadWorkspace action /Param1:value1 /Param2:value2 /Param3:value3 

The parameter without a flag (/  or  -) is interpreted as the name of an action to be executed. All following parameters are passed to the action. Only one action is allowed per command line call.

A script can also contain and register an action. This means that it can also evaluate action parameters.

It is necessary to pass more general command line parameters **before** the action name.

List of general command line parameters evaluated by Eplan:

|  |  |
| --- | --- |
| Parameter | Description |
| /Variant | Select the product variant you want to start. E.g. "Electric P8" or "Fluid" |
| /NoLoadWorkspace | No workspace is loaded or restored. |
| /NoSplash | No splash screen is shown on system start. |
| /Language:en\_us | Eplan is started with GUI language "English". The language predefined in the settings of Eplan will not be changed. |
| /Auto | Eplan is shut down after executing the command line. |
| /Quiet | No dialogs are shown while a command line is being executed. |
| /Frame:0 | - /Frame:0 ' The Eplan main frame is invisible - /Frame:1 ' The Eplan main frame is restored to its original size and position - /Frame:2 ' The Eplan main frame is started minimized - /Frame:3 ' The Eplan main frame is started maximized |
| /Setup | All Settings are restored to their installation default |
| <action name> | The action will be executed, all following parameters (starting with  /  or  ') are passed to the action as parameters. |

Any command line parameter after the action name is passed as parameter to the action. The parameters are wrapped into an  ActionCallingContext  as string parameters and can be extracted by the action. Please note that the parameter names on the command line and in the  ActionCallingContext  must be spelled in the exactly the same:

EPLAN.EXE /Variant:"Electric P8" action /Param1:value1 /Param2:value2 /Param3:value3 

**C#**
```csharp
public bool Execute(ActionCallingContext ctx )

{

   String strParamValue1=null;

   ctx.GetParameter("Param1", ref strParamValue1);

   String strParamValue2=null;

   ctx.GetParameter("Param2", ref strParamValue2);

   String strParamValue3=null;

   ctx.GetParameter("Param3", ref strParamValue3);

   return true;

}

Public Function Execute(ctx As ActionCallingContext) As Boolean Implements IEplAction

   ctx.GetParameter("Param1", strParamValue1)

   ctx.GetParameter("Param2", strParamValue2)

   ctx.GetParameter("Param3", strParamValue3)

   Return True
```

 Warning: When starting Eplan from the command line with an action, then no previously opened projects are opened at the beginning of the session.
