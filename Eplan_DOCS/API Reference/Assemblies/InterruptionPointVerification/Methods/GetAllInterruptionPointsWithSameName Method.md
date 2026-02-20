# GetAllInterruptionPointsWithSameName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.InterruptionPointVerification~GetAllInterruptionPointsWithSameName.html

---

Gets all interruption points with the same name from the project. Can be called within the execute function.

Syntax

**C#**



public void GetAllInterruptionPointsWithSameName( 

   InterruptionPoint oInterruptionPoint,

   ref ArrayList colInterruptionPoints

)

public:

void GetAllInterruptionPointsWithSameName( 

   InterruptionPoint^ oInterruptionPoint,

   ArrayList^% colInterruptionPoints

)


#### Parameters

*oInterruptionPoint*
:   Interruption point with name, for which all other interruption points should be found.

*colInterruptionPoints*
:   List with all interruption points with the same name.

Remarks

This function uses an internal buffer mechanism. You can use this, to get all pairs of interruption points (in pair layout) on one potential.
