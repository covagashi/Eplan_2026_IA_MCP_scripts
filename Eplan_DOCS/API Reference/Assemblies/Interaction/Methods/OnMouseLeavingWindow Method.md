# OnMouseLeavingWindow Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnMouseLeavingWindow.html

---

Is called after Mouse leave the window.

Syntax

**C#**



public virtual RequestCode OnMouseLeavingWindow( 

   Position pos

)

public:

virtual RequestCode OnMouseLeavingWindow( 

   Position^ pos

)


#### Parameters

*pos*

#### Return Value

Default [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html) for this function is `Nothing`.

Remarks

This method is invoke while dragging operation if [OnStartDrag](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnStartDrag.html) returned [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html).
