# Step Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Progress~Step.html

---

Uses a step

Syntax

**C#**



public void Step( 

   int nSteps

)

public:

void Step( 

   int nSteps

)


#### Parameters

*nSteps*
:   Number of steps to be used.

Remarks

Please not use the method when a nested EPLAN progress (i.e. from API method) could be called afterwards.
