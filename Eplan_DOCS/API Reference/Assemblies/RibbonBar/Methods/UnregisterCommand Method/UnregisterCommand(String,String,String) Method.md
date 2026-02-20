# UnregisterCommand(String,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~UnregisterCommand(String,String,String).html

---

Removes a command from the ribbon. If the ribbon doesn't exist yet, the command will be removed after the system start is finished

Syntax

**C#**



public void UnregisterCommand( 

   string strActionCommandLine,

   string tabName,

   string commandGroupName

)

public:

void UnregisterCommand( 

   String^ strActionCommandLine,

   String^ tabName,

   String^ commandGroupName

)


#### Parameters

*strActionCommandLine*
:   Object which are used as a template for a new ribbon command

*tabName*
:   The name of the tab

*commandGroupName*
:   The name of the command group

Remarks

If tabName or commandGroupName is empty, the command is removed from the command group Extensions->API
