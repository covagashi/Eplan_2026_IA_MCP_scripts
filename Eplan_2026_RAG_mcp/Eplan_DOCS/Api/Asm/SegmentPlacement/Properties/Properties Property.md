# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacement~Properties.html

---

EPLAN properties of the SegmentPlacement object.

Syntax

**C#**



public new SegmentPlacementPropertyList Properties {get;}

public:

new property SegmentPlacementPropertyList^ Properties {

   SegmentPlacementPropertyList^ get();

}


Example

**C#**

```
Function func;

func.Properties[Properties.Function.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.Function.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.Function.FUNC_DEVICETAG_FULL];
```
