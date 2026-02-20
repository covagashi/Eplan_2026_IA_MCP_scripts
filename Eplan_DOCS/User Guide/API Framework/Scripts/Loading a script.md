# Loading a script

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/RegisterAScript.html

---

You can load and unload scripts in Eplan. In this case, not the start function is executed, but special functions are registered in Eplan. You can add a new action to Eplan, add ribbon buttons to the Extension ribbon > API command group, and register functions to react on Eplan events.

The following example shows a script that registers a new action. Therefore, a function is marked by the attribute  [DeclareAction]. The parameter of the attribute defines the name of the new action in Eplan.

**C#**
```csharp
public class SimpleScriptAction

{

     [DeclareAction("MyScriptAction")]

     public void MyFunctionAsAction()

     {

           new Decider().Decide(EnumDecisionType.eOkDecision, "MyFunctionAsAction was called!", "RegisterScriptAction", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

           return;

     }

}

Public Class SimpleScriptAction

   <DeclareAction("MyScriptAction")>  _

      dec.Decide(EnumDecisionType.eOkDecision, "MyFunctionAsAction was called!", "RegisterScriptAction", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)
```

When a script with the above code is loaded, the function "MyFunctionAsAction" is registered in Eplan as action by the name "MyScriptAction". The new action can now be used like any other action in Eplan. For example, it can be called from the command line or assigned to a button.

Once the script has been loaded, it will be automatically loaded during the Startup of Eplan and the action will be available again.

To unload or unregister a script, you just call the ribbon File > Extras > Interfaces > [Scripts](Scripts.html) > Unload and select the respective script in the dialog:

