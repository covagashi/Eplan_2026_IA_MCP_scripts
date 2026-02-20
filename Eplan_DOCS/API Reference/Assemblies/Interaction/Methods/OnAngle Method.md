# OnAngle Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnAngle.html

---

Is called after input of an angle by the user.

Syntax

**C#**



public virtual RequestCode OnAngle( 

   double dAngle

)

public:

virtual RequestCode OnAngle( 

   double dAngle

)


#### Parameters

*dAngle*

#### Return Value

Default [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html) for this function is `Stop`.

Remarks

If this interaction needs an angle, the graphical editor changes to an angle input mode. In this case, the user has define an angle by a click into the CAD window or by typing the angle into the command line window. Value is in radians.
