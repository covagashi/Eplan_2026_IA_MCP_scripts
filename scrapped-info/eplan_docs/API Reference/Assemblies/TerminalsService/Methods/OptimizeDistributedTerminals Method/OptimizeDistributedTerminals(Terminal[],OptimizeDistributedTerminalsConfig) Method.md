# OptimizeDistributedTerminals(Terminal[],OptimizeDistributedTerminalsConfig) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1452.html

---

Optimize all distributed terminals of the selected terminals

Syntax

**C#**



public bool OptimizeDistributedTerminals( 

   Terminal[] arrTerminals,

   TerminalsService.OptimizeDistributedTerminalsConfig settings

)

public:

bool OptimizeDistributedTerminals( 

   array<Terminal^>^ arrTerminals,

   TerminalsService.OptimizeDistributedTerminalsConfig^ settings

)


#### Parameters

*arrTerminals*
:   Array of terminals to process.

*settings*
:   A set of options for optimization process. If NULL, options last used in GUI are read from user settings.

#### Return Value

TRUE if operation succeeded, FALSE otherwise.
