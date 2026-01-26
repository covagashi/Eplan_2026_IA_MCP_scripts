# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningObject~Properties.html

---

EPLAN properties of the PlanningObject object.

Syntax

**C#**



public new PlanningObjectPropertyList Properties {get;}

public:

new property PlanningObjectPropertyList^ Properties {

   PlanningObjectPropertyList^ get();

}


Example

**C#**

```
Function func;

func.Properties[Properties.Function.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.Function.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.Function.FUNC_DEVICETAG_FULL];
```
