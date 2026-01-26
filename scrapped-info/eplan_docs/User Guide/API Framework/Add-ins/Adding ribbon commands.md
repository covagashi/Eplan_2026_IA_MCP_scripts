# Adding ribbon commands

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/AddingRibbonCommand.html

---

An add-in can add one or more ribbon commands to the Extensions > API command gropup. Therefore the class  Eplan.EplApi.Gui.RibbonBar  provides a function  AddCommand  which should be called in the  OnRegister()  method of the add-in class:

**C#**
```csharp
/// <summary>

/// The function is called once during registration add-in.

/// </summary>

/// <param name="bLoadOnStart"> true: In the next Eplan session, add-in will be loaded during initialization</param>

/// <returns></returns>

public bool OnRegister(ref System.Boolean bLoadOnStart)

{

   var ribbonBar= new Eplan.EplApi.Gui.RibbonBar();

   ribbonBar.AddCommand("CSharpAction", "CSharpAction");

   return true;

}

/// <summary>

/// The function is called during unregistration the add-in.

/// </summary>

/// <returns></returns>

public bool OnUnregister()

{

    var ribbonBar = new Eplan.EplApi.Gui.RibbonBar();

    return ribbonBar.RemoveCommand("CSharpAction");

}

   ribbonBar.AddCommand("CSharpAction", "CSharpAction")

   Return True

Public Function OnUnregister() As Boolean Implements IEplAddIn.OnUnregister

    Return ribbonBar.RemoveCommand("CSharpAction")
```

The function  AddCommand(text, command line)  adds a button (i.e ribbon command) with the text "CSharpAction" and assigns the action "CSharpAction" to it. The button is then visible in Extensions > API command group. It is also possible to add it to a custom command group that exists in either a persistent tab or a custom tab.

Ribbon commands are always assigned to an action. This can be either a custom action (created using the API) or an already existing action.
