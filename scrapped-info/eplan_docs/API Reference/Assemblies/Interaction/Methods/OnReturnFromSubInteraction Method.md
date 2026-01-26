# OnReturnFromSubInteraction Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnReturnFromSubInteraction.html

---

Is called on end of sub-interaction.

Syntax

**C#**



public virtual RequestCode OnReturnFromSubInteraction( 

   bool bSuccessFull,

   Interaction pSubInteraction

)

public:

virtual RequestCode OnReturnFromSubInteraction( 

   bool bSuccessFull,

   Interaction^ pSubInteraction

)


#### Parameters

*bSuccessFull*
:   If `true` sub-interaction finish with [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html).

*pSubInteraction*

#### Return Value

Default [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html) for this function is `Nothing`.
