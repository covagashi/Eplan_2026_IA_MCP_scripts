# GetCommands Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonCommandGroup~GetCommands.html

---

Returns commands of the command group

Syntax

**C#**



public Dictionary<uint,RibbonCommand> GetCommands( 

   bool bIgnoreDummeItems

)

public:

Dictionary<uint,RibbonCommand^>^ GetCommands( 

   bool bIgnoreDummeItems

)


#### Parameters

*bIgnoreDummeItems*
:   Determines whether dummy commands should be ignored

#### Return Value

Returns commands of the command group in the form ID (key) and a RibbonCommand (value)
