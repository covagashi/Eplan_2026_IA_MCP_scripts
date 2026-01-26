# Ribbon bar

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/TheRibbon.html

---

Since version 2022, the Eplan GUI items are accessible through a ribbon. In the API this control is represented by the following classes:

- Eplan.EplApi.Gui.RibbonBar
- Eplan.EplApi.Gui.RibbonTab
- Eplan.EplApi.Gui.RibbonCommandGroup
- Eplan.EplApi.Gui.RibbonCommand

The ribbon is divided into tabs and these tabs into command groups and commands.

All ribbon related classes are stored in the  Eplan.EplApi.Gui  namespace. They correspond to the types of ribbon items from the GUI:

Here is an example of listing ribbon items (tabs, command groups and commands):

**C#**

```


RibbonBar ribbonBar = new RibbonBar();

foreach (RibbonTab tab in ribbonBar.Tabs)

{

    Debug.WriteLine($"\tTab Name:{tab.Name}------------");

    foreach (var commandGroup in tab.CommandGroups)

    {

        Debug.WriteLine($"\t\tCommand group:{commandGroup.Name}------");

        foreach (var command in commandGroup.Commands)

        {

            RibbonCommand ribbonCommand = command.Value;

            uint commandId          = ribbonCommand.ID;

            string strText          = ribbonCommand.Text;

            string strDescription   = ribbonCommand.Description;

            string strTooltipText   = ribbonCommand.TooltipText;

            string strActionCommandLine = ribbonCommand.ActionCommandLine;

            Debug.WriteLine($"\t\t\tCommand Id:{commandId}---.Text:{strText}---.ActionCommandLine:{strActionCommandLine}---.TooltipText:{strTooltipText}---.Description:{strDescription}");

        }

        Debug.WriteLine($"\t\t-----------------------");

    }

    Debug.WriteLine($"\t-----------------------------");

}

```

Please keep it in mind that some tabs are context sensitive, i.e they are open only when the editor is visible.

The old menu and toolbars are no longer accessible. The equivalent of the old menu point / toolbar button is now the ribbon command:

In the API, commands can be created in following places:

- Extensions > API command group
- A custom command group that is placed in a persistient tab or a custom tab

### Menu and toolbar migration

The classes corresponding to the old GUI items i.e.  Toolbar  and  Menu  are currently deprecated, so it is highly recommended to migrate relevant code.

The following table shows how to create new ribbon items and provides example code:

| Old GUI item | Old API method | New GUI equivalent | New API method | Example old code | Example new code |
| --- | --- | --- | --- | --- | --- |
| Main menu | Menu.AddMainMenu | RibbonTab | RibbonBar.AddTab | menu.AddMainMenu("API Tests A-N", Menu.MainMenuName.eMainMenuHelp,"AddingMessageAction", "AddingMessageAction", "First menu element", 1); | var ribbonTab = ribbonBar.AddTab("API Tests A-N"); |
| Popup menu | Menu.AddPopupMenuItem | RibbonCommandGroup | RibbonTab.AddCommandGroup | menu.AddPopupMenuItem("ActionExample - test2","ActionExample - test2 submenupoint1", "ActionExample", "status text", mainID, 0, false, false); | var commandGroup = ribbonTab.AddCommandGroup("ActionExample - test2"); |
| Toolbar | toolbar.CreateCustomToolbar | RibbonCommandGroup | RibbonTab.AddCommandGroup | toolbar.CreateCustomToolbar("SelectionSet", Toolbar.ToolBarDockPos.eToolbarLeft, 4, 1, true); | var commandGroup = ribbonTab.AddCommandGroup("SelectionSet"); |
| Menu item | menu.AddMenuItem( | RibbonCommand | RibbonBar.AddCommand , RibbonCommandGroup.AddCommand | menu.AddMenuItem("UndoAction", "UndoAction");  menu.AddMenuItem("SelectionRecursive", "SelectionRecursiveAction", "", selectionSetID, 1,false, false); | ribbonBar.AddCommand("UndoAction", "UndoAction");  commandGroup.AddCommand("SelectionRecursive", "SelectionRecursiveAction"); |
| Toolbar button | toolbar.AddButton( | RibbonCommand | RibbonCommandGroup.AddCommand('¦,index) | toolbar.AddButton("SelectionSet", Int32.MaxValue, "SelectionOneItemAction","C:\\myicons\\0.ico", "SelectionOneItemAction"); | commandGroup.AddCommand("SelectionOneItemAction", "SelectionOneItemAction", 0); |

Here is also a list of other old methods and their new counterparts:

|  |
| --- |
|  |
| Old method | New method |
| Toolbar.ExistsToolbar | RibbonBar.Tabs.Any(by LINQ)  RibbonBar.GetTab  RibbonBar.GetDefaultTab |
| Toolbar.GetButtonAction | RibbonCommand.ActionCommandLine |
| Toolbar.GetButtonToolTip | RibbonCommand.TooltipText |
| Toolbar.GetCountOfButtons | RibbonCommandGroup.Commands.Count |
| Toolbar.GetPersistentButtonId  Menu.GetCustomMenuId  GetPersistentMenuId | RibbonCommand.ID |
| Toolbar.RemoveButton | RibbonCommand.Remove |
| Toolbar.RemoveCustomToolbar | RibbonCommandGroup.Remove |
| Menu.IsActionChecked | RibbonCommand.IsChecked |
| Menu.IsActionEnabled | RibbonCommand.IsEnabled |
| Menu.RemoveMenuItem | RibbonTab.Remove  RibbonCommandGroup.Remove  RibbonCommand.Remove |

The  ContextMenu  class is not affected by this change, i.e everything should work as before version 2022.

For more information, please refer to chapter "The New Ribbon" of the Eplan Help.

### RibbonIcons

Ribbon command actions can now be created with  .svg  icons. There is a list of standard  CommandIcons, accessible by name or index number.  
Furthermore, below examples present also how to use custom icons, which can be added by specifying path to  .svg  file or providing icon content in string format.

Adding standard icons

**C#**

```


var ribbonBar = new RibbonBar();

var tab = ribbonBar.AddTab("RibbonIcons");

// Adding standard icons to a command action using enum names

var commandGroup = tab.AddCommandGroup("enum names");

commandGroup.AddCommand("Button1", "action1", new RibbonIcon(CommandIcon.Generator));

commandGroup.AddCommand("Button2", "action2", new RibbonIcon(CommandIcon.Amplifier));

commandGroup.AddCommand("Button3", "action3", new RibbonIcon(CommandIcon.Octagon_3));

// Adding standard icons to a command action using index numbers

commandGroup = tab.AddCommandGroup("index numbers");

commandGroup.AddCommand("Button4", "action4", new RibbonIcon(75));

commandGroup.AddCommand("Button5", "action5", new RibbonIcon(123));

commandGroup.AddCommand("Button6", "action6", new RibbonIcon(181));

```

Adding custom icons

**C#**

```


// Adding new custom icons to a command action using the path to the file

commandGroup = tab.AddCommandGroup("custom icons path to file");

commandGroup.AddCommand("Button7", "action7", new RibbonIcon("D:\\Icon2.svg"));

commandGroup.AddCommand("Button8", "action8", new RibbonIcon("D:\\Icon3.svg"));

// Adding new custom icons to a RibbonBar using the path to the file

RibbonIcon ribbonIcon = ribbonBar.AddIcon("D:\\CarIco.svg");

commandGroup = tab.AddCommandGroup("AddIcon using path");

commandGroup.AddCommand("Button10", "action10", ribbonIcon);

// Adding new custom icons to a RibbonBar using the string source

var svgContent = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" viewBox=\"0 0 16 16\">" +

 "<title>Clock_1</title>" +

 "<g id=\"GUIicons\">" +

 "<g id=\"Clock\">" +

 "<g>" +

   "<circle cx=\"8\" cy=\"8\" r=\"7.5\" style=\"fill: #fff\"/>" +

   "<path d=\"M8,1A7,7,0,1,1,1,8,7,7,0,0,1,8,1M8,0a8,8,0,1,0,8,8A8,8,0,0,0,8,0Z\" style=\"fill: #4a7db1\"/>" +

 "<g>" +

   "<path d=\"M12,8.5H8v-1h4ZM7.5,4V7h1V4Z\" style=\"fill:#9e0b0f\"/>" +

 "<g>" +

   "<rect x=\"13.5\" y=\"7\" width=\"1\" height=\"2\"transform=\"translate(22 -6) rotate(90)\" style=\"fill: #505050\"/>" +

   "<rect x=\"7.5\" y=\"13\" width=\"1\" height=\"2\"transform=\"translate(16 28) rotate(-180)\" style=\"fill: #505050\"/>" +

   "<rect x=\"1.5\" y=\"7\" width=\"1\" height=\"2\"transform=\"translate(-6 10) rotate(-90)\" style=\"fill: #505050\"/>" +

   "<rect x=\"7.5\" y=\"1\" width=\"1\" height=\"2\"style=\"fill: #505050\"/>" +

 "</g>" +

   "<circle cx=\"8\" cy=\"8\" r=\"1\" style=\"fill:#4a7db1;stroke: #9e0b0f;stroke-miterlimit: 10;stroke-width: 0.5px\"/>" +

 "</g>" +

 "</g>" +

 "</svg>";

commandGroup = tab.AddCommandGroup("AddIcon using source");

ribbonIcon = ribbonBar.AddIcon(svgContent);

commandGroup.AddCommand("Button13", "action13", ribbonIcon);

```

The above examples result in this RibbonBar:

**RibbonCommandInfo**

Ribbon command actions can now be created using a  RibbonCommandInfo  object. This object contains all required and optional properties.

The optional properties are  Description,  Tooltip,  Icon,  IndexButtonPosition,  MultiLangButtonText,  MultiLangDescription  and  MultiLangTooltip.

The multilanguage properties are used over the non-multilanguage properties if they are not empty.

The IndexButtonPosition is used to specify the position in a  RibbonCommandGroup.

**C#**

```


// Adding new commands using the RibbonCommandInfo

commandGroup = tab.AddCommandGroup("commands with RibbonCommandInfo");

RibbonCommandInfo ribbonCommandInfo = new RibbonCommandInfo("buttonText", "actionCommandLine");

commandGroup.AddCommand(ribbonCommandInfo);

```

**Add existing Eplan actions to a custom CommandGroup**

It is possible to add existing Eplan ribbon command actions to a custom  CommandGroup  via their  Command.ID.

The corresponding internal icon is automatically added to the action.

**C#**

```


// Adding an existing Eplan command action by its ID

const int commandId = 35089;

var tab = ribbonBar.AddTab("CustomTab");

var commandGroup = tab.AddCommandGroup("Group1");

var commandAction = commandGroup.AddCommandWithId(commandId);

```

To find the correct  Command.ID  value for the command, you can check the description log in the Eplan Diagnostics dialog after calling this action from the ribbon (to show the Diagnostics Dialog press [Ctrl] + [VK\_OEM\_5]. [VK\_OEM\_5] corresponds to the [^] key on a German keyboard or to the [\] on a United States 101 keyboard.):

**SVG Icons limitations**

Our UI libraries provide  SVG  support with the following limitations:

   '¢ Scripts, interactions and external objects are not implemented for security reasons.

   '¢ Animations, videos, sounds and internal images are not implemented.

   '¢ Since  SVG  icons should be small and fast to render, we disabled the following  SVG  elements that can significantly affect drawing performance:  
  
       -  <pattern>  
  
       -  <color-profile>  
  
       -  <hkern>  
  
       -  <hatch>  
  
       -  <hatchpath>  
  
       -  all effects, blend mode and filters

       -  compressed  SVG  files (SVGz)

It is strongly recommended to use only simplified ("optimized")  SVG: All elements such as text or shapes should be converted to paths and all paths should be combined.  
The simplified  SVG  is small and fast-drawing. In addition, it will be very difficult to "reverse engineer" your media in this case.
