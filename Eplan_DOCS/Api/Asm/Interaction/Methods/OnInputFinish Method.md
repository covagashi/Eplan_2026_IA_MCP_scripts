# OnInputFinish Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnInputFinish.html

---

Is called after special input operation has finished.

Syntax

**C#**



public virtual RequestCode OnInputFinish()

public:

virtual RequestCode OnInputFinish();


#### Return Value

Default [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html) for this function is `Nothing`.

Remarks

For example the input sequence of the vertexes for a polyline. Usually this function is called, when the user has pressed the SPACE key.
