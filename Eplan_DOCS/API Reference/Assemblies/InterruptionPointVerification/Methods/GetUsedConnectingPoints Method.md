# GetUsedConnectingPoints Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.InterruptionPointVerification~GetUsedConnectingPoints.html

---

Gets all used connection points from the project. Can be called within the execute function.

Syntax

**C#**



public void GetUsedConnectingPoints( 

   InterruptionPoint oInterruptionPoint,

   ref ArrayList colUsedConnectingPoints

)

public:

void GetUsedConnectingPoints( 

   InterruptionPoint^ oInterruptionPoint,

   ArrayList^% colUsedConnectingPoints

)


#### Parameters

*oInterruptionPoint*
:   Interruption point, for which all other connection points should be found.

*colUsedConnectingPoints*
:   The result list with all used connection points.

Remarks

This function uses an internal buffer mechanism.
