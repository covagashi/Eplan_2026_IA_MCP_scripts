# AddCommand(String,String,RibbonIcon) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonCommandGroup~AddCommand(String,String,RibbonIcon).html

---

Adds new command to the command group

Syntax

**C#**



public RibbonCommand AddCommand( 

   string strButtonText,

   string strActionCommandLine,

   RibbonIcon icon

)

public:

RibbonCommand^ AddCommand( 

   String^ strButtonText,

   String^ strActionCommandLine,

   RibbonIcon^ icon

)


#### Parameters

*strButtonText*
:   Text that is set at a button

*strActionCommandLine*
:   Command line of the action

*icon*
:   Ribbon icon object which are used to create icon based on it

#### Return Value

Created command, or null if nothing was created

Remarks

The method can add a command only to a custom group.
