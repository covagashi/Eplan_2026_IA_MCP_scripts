# RibbonBar

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar.html

---

Represents ribbon bar control.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Gui.RibbonBar**

Syntax

**C#**



public class RibbonBar

public ref class RibbonBar


Remarks

The RibbonBar represents the whole ribbon bar control. All elements belonging to it are accessible through RibbonBar class. They are represented by classes RibbonTab, RibbonCommandGroup and RibbonCommand. For more information, please refer to "Ribbon bar" chapter of API Help or "The New Ribbon" chapter of Eplan Platform Help.

Example

Example below shows how to avoid GUI flickering and make sure that RibbonBar will be refreshed just after the add operations are completed. Parameter refreshAfterChanges=true means that refresh will be executed only once on RibbonBar destructor, in this case at the end of using() statement. This technique can be used also for removing elements from RibbonBar.

**C#**

```
using (var ribbonBar = new RibbonBar(true))

{

    var ribbonTab = ribbonBar.GetTab("MyTab1") ?? ribbonBar.AddTab("MyTab1");

    var commandGroup = ribbonTab.AddCommandGroup("MyExampleActions");

    commandGroup.AddCommand("MyExampleAction1", "ExampleAction /Parameter:1");

    commandGroup.AddCommand("MyExampleAction2", "ExampleAction /Parameter:2");

    commandGroup.AddCommand("MyExampleAction3", "ExampleAction /Parameter:3");

}

```

Example of adding a command to the last position of the ribbon

- [c#](#i-tab-content-e865deaa-e961-4c75-8ff6-6b75f79477c7)

```
RibbonBar ribbonBar = new RibbonBar();

ribbonBar.AddCommand("New ribbon button text", "XPartsManagementStart", new RibbonIcon(CommandIcon.Circle_0));
```

Example of adding a tab, command group and a command

- [c#](#i-tab-content-5b0d4237-57ae-4c5a-ba06-834b463dcd93)

```
var newTab = new Eplan.EplApi.Gui.RibbonBar().AddTab("New API tab");

var commandGroup = newTab.AddCommandGroup("New API command group");

var command = commandGroup.AddCommand("New API command", "XPartsManagementStart");
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [RibbonBar Constructor](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ActiveTab](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~ActiveTab.html) | Returns active tab |
| Public Property | [Icons](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~Icons.html) | Returns icons of the ribbon bar |
| Public Property | [Tabs](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~Tabs.html) | Returns tabs of the ribbon bar |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddCommand](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~AddCommand.html) | Overloaded. Adds command to the ribbon |
| Public Method | [AddDelayedAction](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~AddDelayedAction.html) | Calls an action object on the ribbon. If the ribbon doesn't exist yet, the action will be executed after the system start is finished |
| Public Method | [AddIcon](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~AddIcon.html) | Adds new icon to the ribbon bar |
| Public Method | [AddTab](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~AddTab.html) | Overloaded. Adds a new tab to the ribbon |
| Public Method | [Dispose](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~Dispose().html) | Destructor for deterministic finalization of MainRibbon object. |
| Public Method | [GetDefaultTab](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~GetDefaultTab.html) | Returns default tab |
| Public Method | [GetTab](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~GetTab.html) | Overloaded. Returns tab by name, multilanguage |
| Public Method | [RegisterCommand](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~RegisterCommand.html) | Overloaded. Adds a command to the ribbon. If the ribbon doesn't exist yet, the command will be added after the system start is finished |
| Public Method | [RemoveCommand](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~RemoveCommand.html) | Removes command from Extensions->API group |
| Public Method | [RemoveIcon](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~RemoveIcon.html) | Removes custom icon from the ribbon bar |
| Public Method | [UnregisterCommand](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~UnregisterCommand.html) | Overloaded. Removes a command from the ribbon. If the ribbon doesn't exist yet, the command will be removed after the system start is finished |


