# OnEndDrag Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnEndDrag.html

---

Is called after end of a dragging operation.

Syntax

**C#**



public virtual RequestCode OnEndDrag( 

   bool bSuccess,

   Position oPosition

)

public:

virtual RequestCode OnEndDrag( 

   bool bSuccess,

   Position^ oPosition

)


#### Parameters

*bSuccess*
:   if bSuccess == false, dragging was aborted by user

*oPosition*
:   Current position of cad cursor.

#### Return Value

Default [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html) for this function is `Nothing`.
