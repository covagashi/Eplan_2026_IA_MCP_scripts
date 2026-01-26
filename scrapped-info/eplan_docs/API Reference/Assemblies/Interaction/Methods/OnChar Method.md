# OnChar Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnChar.html

---

Is called after keyboard inputs by the user.

Syntax

**C#**



public virtual RequestCode OnChar( 

   Position oPosition,

   char c

)

public:

virtual RequestCode OnChar( 

   Position^ oPosition,

   char c

)


#### Parameters

*oPosition*
:   Is the current position of CAD cursor.

*c*

#### Return Value

Default [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html) for this function is `Nothing`.
