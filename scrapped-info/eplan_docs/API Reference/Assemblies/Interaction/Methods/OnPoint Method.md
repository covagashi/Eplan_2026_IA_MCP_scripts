# OnPoint Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnPoint.html

---

Is called after a point input by user via mouse or keyboard. That means, that the user has clicked into the CAD Window or opened the command line and input the coordinates of a point.

Syntax

**C#**



public virtual RequestCode OnPoint( 

   Position oPosition

)

public:

virtual RequestCode OnPoint( 

   Position^ oPosition

)


#### Parameters

*oPosition*
:   Current position of cad cursor.

#### Return Value

Default [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html) for this function is `Stop`.

Remarks

This call can occur only, if the Interaction needs the coordinates of a point. In this case, the graphical editor changes into point input mode. A mouse click has then the following result: The coordinates of the mouse position will be translated into world coordinates. Depending on Settings, the system may look for grid points or snap points
