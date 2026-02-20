# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.Vessel~Properties.html

---

EPLAN properties of the Vessel object.

Syntax

**C#**



public new VesselPropertyList Properties {get;}

public:

new property VesselPropertyList^ Properties {

   VesselPropertyList^ get();

}


Example

**C#**

```
Function func;

func.Properties[Properties.Function.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.Function.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.Function.FUNC_DEVICETAG_FULL];
```
