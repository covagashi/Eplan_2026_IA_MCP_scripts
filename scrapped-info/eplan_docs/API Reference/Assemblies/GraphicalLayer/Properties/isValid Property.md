# isValid Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~isValid.html

---

Checks, if layer object is attached to existing project's layer.

Syntax

**C#**



public bool isValid {get;}

public:

property bool isValid {

   bool get();

}


#### Property Value

true : Attached

false : Not attached

Remarks

It may happen that property return false for default Eplan layer. Then it is necessary to [Store](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~Store.html) layer first.
