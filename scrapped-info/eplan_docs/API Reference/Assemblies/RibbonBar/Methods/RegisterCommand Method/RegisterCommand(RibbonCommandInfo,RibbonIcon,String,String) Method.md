# RegisterCommand(RibbonCommandInfo,RibbonIcon,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~RegisterCommand(RibbonCommandInfo,RibbonIcon,String,String).html

---

Adds a command to the ribbon. If the ribbon doesn't exist yet, the command will be added after the system start is finished

Syntax

**C#**



public void RegisterCommand( 

   RibbonCommandInfo ribbonCommandInfo,

   RibbonIcon icon,

   string tabName,

   string commandGroupName

)

public:

void RegisterCommand( 

   RibbonCommandInfo^ ribbonCommandInfo,

   RibbonIcon^ icon,

   String^ tabName,

   String^ commandGroupName

)


#### Parameters

*ribbonCommandInfo*
:   Object which are used as a template for a new ribbon command

*icon*
:   Ribbon icon object which are used to create icon based on it

*tabName*
:   The name of the tab

*commandGroupName*
:   The name of the command group

Remarks

If tabName or commandGroupName is empty, the command is added to the command group Extensions->API
