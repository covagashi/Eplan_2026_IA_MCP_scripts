# Action

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action.html

---

An action performs a task in the system. It is usually called via ribbon items or the command line (see chapter "[Calling actions](CallingActions.html)").  
Parameters can be passed to the action in a context class, and return values can be obtained with this parameter. Actions are implemented in an add-in by deriving a class from the [IEplAction](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAction.html) interface.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.ApplicationFramework.Action**

Syntax

**C#**



public class Action

public ref class Action


Remarks

Actions are registered under a name (see [Name](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~Name.html) property) in the system. Using this name, you can find an action and call its execution function (see [Execute](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~Execute.html) method).  
  
Please mind that Microsoft .NET framework 3.5 contains a class System.Action. If you include the [Eplan.EplApi.ApplicationFramework](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework_namespace.html) namespace in your code file by e.g. a using statement without the use of an alias, you might get a compiler error like:  
"'Action' is an ambiguous reference between 'System.Action' and 'Eplan.EplApi.ApplicationFramework.Action'".  
  
Action names must not contain a period (".").

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Action Constructor](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~_ctor(AfAction).html) | For internal use only. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ActionProperties](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~ActionProperties.html) | Descriptive data for this action. |
| Public Property | [ModuleName](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~ModuleName.html) | Name of the module in which this action is implemented. |
| Public Property | [Name](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~Name.html) | Name used to identify this action in the system. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Execute](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~Execute.html) | Performs the actual action. |
| Public Method | [GetChecked](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~GetChecked.html) | Returns 'checked' state of an action |
| Public Method | [GetEnabled](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action~GetEnabled.html) | Returns whether an action is enabled |


