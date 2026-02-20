# Adding ribbon items by a script

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/script_ribbon.html

---

A script can add one or more items to the Elpan ribbon. The convenient place to add these items is a function with  [DeclareRegister]  attribute, then the items are registered until the script is unloaded:

**C#**

```


public class RegisterRibbonItems

{   

    string m_newTabName         = "New API tab";

    string m_commandGroupName   = "New API command group";

    string m_commandName        = "New API command";

    [DeclareRegister]

    public void registerRibbonItems()

    {               

        cleanItems();

        var newTab = new Eplan.EplApi.Gui.RibbonBar().AddTab(m_newTabName);

        var commandGroup = newTab.AddCommandGroup(m_commandGroupName);                              

        var command = commandGroup.AddCommand(m_commandName, "XPartsManagementStart");

    }

    [DeclareUnregister]

    public void unRegisterRibbonItems()

    {   

        cleanItems();

    }

    void cleanItems()

    {

        var newTab = new Eplan.EplApi.Gui.RibbonBar().Tabs.FirstOrDefault(item => item.Name == m_newTabName);

        if(newTab != null)

            newTab.Remove();

    }   

}

```

Removing a ribbon tab also removes its command groups and commands. Similarly, removing a command group also removes its commands.

A ribbon command is always connected with an action, which is called when the command is clicked. This means that either the script registers an additional action, or the command is assigned to an already existing action.

Remarks

Please mind that users may start Eplan in QUIET mode using  W3u.exe /Quiet  or the API could be initialized by an [offline program](UsingEplanAssemblies.html). Because of this, it is not recommended to show .NET dialogs in the method marked by  [DeclareRegister]. Please use  Eplan.EplApi.Base.Decider  class instead. If you encounter some problem during registering or initializing of a script, just create and throw a  BaseException  or use  BaseException.FixMessage(...)  to add the message to the system messages list.

The following example shows a script, which registers an action and a ribbon command.

**C#**
```csharp
public class ButtonWithAction

{

    [DeclareAction("HelloWorldAction")]

    public void MyFunctionAsAction()

    {

       new Decider().Decide(EnumDecisionType.eOkDecision, "Hello World!", "HelloWorldAction title", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

       return;

    }

    [DeclareRegister]

    public void registerButtonWithAction()

    {

        var ribbonBar= new Eplan.EplApi.Gui.RibbonBar();

        ribbonBar.AddCommand("MyMenuText", "HelloWorldAction", 2);

    }

    [DeclareUnregister]

    public void unRegisterButtonWithAction()

    {

        var ribbonBar= new Eplan.EplApi.Gui.RibbonBar();

        ribbonBar.RemoveCommand("HelloWorldAction");

    }

}

Public Class ButtonWithAction

   <DeclareAction("HelloWorldAction")>  _

      dec.Decide(EnumDecisionType.eOkDecision, "Hello World!", "HelloWorldAction title", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)

      Return

   <DeclareRegister()>  _

      ribbonBar.AddCommand("MyMenuText", "HelloWorldAction", 2)

   <DeclareUnregister()>  _

      ribbonBar.RemoveCommand("HelloWorldAction")
```

The  [DeclareRegister]  attribute calls the function  buttonWithAction()  when the script is loaded. The function creates a new ribbon command "MyMenuText" and binds the action "HelloWorldAction" to it.

Possible problems with flickering and how to avoid them

When loading or unloading a script in which many ribbon items (tabs, command groups and commands) are added, a temporary flickering of the page navigator and other parts of the GUI may occur. The following procedure reduces this flickering to a minimum:

First, create a new RibbonBar object using the constructor that takes the boolean  executeApplyAfterChanges  parameter and set this parameter to "true".  
Then, add all of your custom tabs, command groups and commands to this RibbonBar object, as in the following example:

**C#**

```


public class RegisterRibbonItems

{   

    // Create the RibbonBar object and set the "executeApplyAfterChanges" parameter in the constructor to "true"

    Eplan.EplApi.Gui.RibbonBar myRibbonBar = new Eplan.EplApi.Gui.RibbonBar(true);

    string m_newTabName1        = "New API tab 1";

    string m_newTabName2        = "New API tab 2";

    string m_newTabName3        = "New API tab 3";

    string m_commandGroupName1  = "New API command group 1";

    string m_commandGroupName2  = "New API command group 2";

    string m_commandGroupName3  = "New API command group 3";

    string m_commandGroupName4  = "New API command group 4";

    string m_commandName1       = "New API command 1";

    string m_commandName2       = "New API command 2";

    string m_commandName3       = "New API command 3";

    string m_commandName4       = "New API command 4";

    string m_commandName5       = "New API command 5";

    string m_commandName6       = "New API command 6";

    string m_commandName7       = "New API command 7";      

    [DeclareRegister]

    public void registerRibbonItems()

    {              

        cleanItems();

        // Add all the tabs to the RibbonBar object defined above 

        var newTab1 = myRibbonBar.AddTab(m_newTabName1);

        var newTab2 = myRibbonBar.AddTab(m_newTabName2);

        var newTab3 = myRibbonBar.AddTab(m_newTabName3);

        // Add all the command groups and commands to these tabs

        var commandGroup1 = newTab1.AddCommandGroup(m_commandGroupName1);     

        var commandGroup2 = newTab2.AddCommandGroup(m_commandGroupName2);  

        var commandGroup3 = newTab3.AddCommandGroup(m_commandGroupName3);    

        var commandGroup4 = newTab3.AddCommandGroup(m_commandGroupName4);

        var command1 = commandGroup1.AddCommand(m_commandName1, "YourActionName1");                        

        var command2 = commandGroup1.AddCommand(m_commandName2, "YourActionName2");

        var command3 = commandGroup2.AddCommand(m_commandName3, "YourActionName3");                        

        var command4 = commandGroup3.AddCommand(m_commandName4, "YourActionName4");

        var command5 = commandGroup4.AddCommand(m_commandName5, "YourActionName5");                        

        var command6 = commandGroup4.AddCommand(m_commandName6, "YourActionName6");

        var command7 = commandGroup4.AddCommand(m_commandName7, "YourActionName7");

    }

    [DeclareUnregister]

    public void unRegisterRibbonItems()

    {   

        cleanItems();

    }

    void cleanItems()

    {

        // Clean up ALL commands, command groups and tabs as shown in the topmost example

    }  

}

```
