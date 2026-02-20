# OptimizeDistributedTerminals(TerminalStrip[],OptimizeDistributedTerminalsConfig) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1451.html

---

Optimize all distributed terminals of the selected terminal strips

Syntax

**C#**



public bool OptimizeDistributedTerminals( 

   TerminalStrip[] arrTerminalStrips,

   TerminalsService.OptimizeDistributedTerminalsConfig settings

)

public:

bool OptimizeDistributedTerminals( 

   array<TerminalStrip^>^ arrTerminalStrips,

   TerminalsService.OptimizeDistributedTerminalsConfig^ settings

)


#### Parameters

*arrTerminalStrips*
:   Array of terminal strips to process.

*settings*
:   A set of options for optimization process. If NULL, options last used in GUI are read from user settings.

#### Return Value

TRUE if operation succeeded, FALSE otherwise.
