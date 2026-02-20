# AddCommand(String,String,String,String,RibbonIcon) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonCommandGroup~AddCommand(String,String,String,String,RibbonIcon).html

---

Adds new command to the command group

Syntax

**C#**



public RibbonCommand AddCommand( 

   string strButtonText,

   string strActionCommandLine,

   string tooltip,

   string description,

   RibbonIcon icon

)

public:

RibbonCommand^ AddCommand( 

   String^ strButtonText,

   String^ strActionCommandLine,

   String^ tooltip,

   String^ description,

   RibbonIcon^ icon

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

*icon*
:   Ribbon icon object which are used to create icon based on it

#### Return Value

Created command, or null if nothing was created

Remarks

The method can add a command only to a custom group.
