# AddCommand(RibbonCommandInfo) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonCommandGroup~AddCommand(RibbonCommandInfo).html

---

Adds new command to the command group. Use this method preferably!

Syntax

**C#**



public RibbonCommand AddCommand( 

   RibbonCommandInfo ribbonCommandInfo

)

public:

RibbonCommand^ AddCommand( 

   RibbonCommandInfo^ ribbonCommandInfo

)


#### Parameters

*ribbonCommandInfo*
:   Object which are used as a template for a new ribbon command

#### Return Value

Created command, or null if nothing was created

Remarks

The method can add a command only to a custom group.
