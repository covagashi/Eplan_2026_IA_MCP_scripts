# AddCommandWithId Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonCommandGroup~AddCommandWithId.html

---

Adds new command to the command group with commandID

Syntax

**C#**



public RibbonCommand AddCommandWithId( 

   uint ribbonCommandId

)

public:

RibbonCommand^ AddCommandWithId( 

   uint ribbonCommandId

)


#### Parameters

*ribbonCommandId*
:   RibbonCommand ID is used to add command to custom Group

#### Return Value

Created command, or null if nothing was created

Remarks

The method can add a command with ID only to a custom group.
