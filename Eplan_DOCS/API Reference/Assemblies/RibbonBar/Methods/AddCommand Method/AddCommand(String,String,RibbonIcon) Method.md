# AddCommand(String,String,RibbonIcon) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~AddCommand(String,String,RibbonIcon).html

---

Adds command to the ribbon

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
:   Command text

*strActionCommandLine*
:   Command line

*icon*
:   Ribbon icon object which are used to create icon based on it

Remarks

The command is added to the command group Extensions->API
