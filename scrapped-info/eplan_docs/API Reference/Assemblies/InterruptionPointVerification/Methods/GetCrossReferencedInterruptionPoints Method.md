# GetCrossReferencedInterruptionPoints Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.InterruptionPointVerification~GetCrossReferencedInterruptionPoints.html

---

Gets all cross reference interruption points with the same name from the project. Can be called within the execute function.

Syntax

**C#**



public void GetCrossReferencedInterruptionPoints( 

   InterruptionPoint oInterruptionPoint,

   ref ArrayList colInterruptionPoints

)

public:

void GetCrossReferencedInterruptionPoints( 

   InterruptionPoint^ oInterruptionPoint,

   ArrayList^% colInterruptionPoints

)


#### Parameters

*oInterruptionPoint*
:   Interruption point with name, for which all other cross reference interruption points should be found.

*colInterruptionPoints*
:   The result list with all cross reference interruption points.

Remarks

This function uses an internal buffer mechanism. You can use this to get all interruption points in a star layout. In pair layout, you get only the one paired interruption point.
