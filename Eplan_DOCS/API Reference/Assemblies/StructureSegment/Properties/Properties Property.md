# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.StructureSegment~Properties.html

---

EPLAN properties of the StructureSegment object.

Syntax

**C#**



public new StructureSegmentPropertyList Properties {get;}

public:

new property StructureSegmentPropertyList^ Properties {

   StructureSegmentPropertyList^ get();

}


Example

**C#**

```
Function func;

func.Properties[Properties.Function.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.Function.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.Function.FUNC_DEVICETAG_FULL];
```
