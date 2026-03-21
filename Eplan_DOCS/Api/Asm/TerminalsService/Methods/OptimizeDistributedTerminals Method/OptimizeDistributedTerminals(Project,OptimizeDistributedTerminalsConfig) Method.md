# OptimizeDistributedTerminals(Project,OptimizeDistributedTerminalsConfig) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1450.html

---

Optimize all distributed terminals of all terminal strips in the project

Syntax

**C#**



public bool OptimizeDistributedTerminals( 

   Project prj,

   TerminalsService.OptimizeDistributedTerminalsConfig settings

)

public:

bool OptimizeDistributedTerminals( 

   Project^ prj,

   TerminalsService.OptimizeDistributedTerminalsConfig^ settings

)


#### Parameters

*prj*
:   A project to process.

*settings*
:   A set of options for optimization process. If NULL, options last used in GUI are read from user settings.

#### Return Value

TRUE if operation succeeded, FALSE otherwise.
