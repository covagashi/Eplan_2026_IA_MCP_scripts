# AddCommand(RibbonCommandInfo,RibbonIcon) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonCommandGroup~AddCommand(RibbonCommandInfo,RibbonIcon).html

---

Adds new command to the command group

Syntax

**C#**



public RibbonCommand AddCommand( 

   RibbonCommandInfo ribbonCommandInfo,

   RibbonIcon icon

)

public:

RibbonCommand^ AddCommand( 

   RibbonCommandInfo^ ribbonCommandInfo,

   RibbonIcon^ icon

)


#### Parameters

*ribbonCommandInfo*
:   Object which are used as a template for a new ribbon command

*icon*
:   Ribbon icon object which are used to create icon based on it

#### Return Value

Created command, or null if nothing was created

Remarks

The method can add a command only to a custom group.
