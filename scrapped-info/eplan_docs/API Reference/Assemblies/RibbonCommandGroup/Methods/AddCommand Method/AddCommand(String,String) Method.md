# AddCommand(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonCommandGroup~AddCommand(String,String).html

---

Adds new command to the command group

Syntax

**C#**



public RibbonCommand AddCommand( 

   string strButtonText,

   string strActionCommandLine

)

public:

RibbonCommand^ AddCommand( 

   String^ strButtonText,

   String^ strActionCommandLine

)


#### Parameters

*strButtonText*
:   Text that is set at a button

*strActionCommandLine*
:   Command line of the action

#### Return Value

Created command, or null if nothing was created

Remarks

The method can add a command only to a custom group.
