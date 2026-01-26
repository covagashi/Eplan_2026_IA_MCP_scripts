# AddCommand(String,String,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonCommandGroup~AddCommand(String,String,String,String).html

---

Adds new command to the command group

Syntax

**C#**



public RibbonCommand AddCommand( 

   string strButtonText,

   string strActionCommandLine,

   string tooltip,

   string description

)

public:

RibbonCommand^ AddCommand( 

   String^ strButtonText,

   String^ strActionCommandLine,

   String^ tooltip,

   String^ description

)


#### Parameters

*strButtonText*
:   Text that is set at a button, multilanguage

*strActionCommandLine*
:   Command line of the action

*tooltip*
:   Tooltip to the command

*description*
:   Description of the command

#### Return Value

Created command, or null if nothing was created

Remarks

The method can add a command only to a custom group.
