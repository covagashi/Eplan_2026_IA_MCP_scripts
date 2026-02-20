# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PCTLoopFunction~Properties.html

---

EPLAN properties of the PCTLoopFunction object.

Syntax

**C#**



public new PCTLoopFunctionPropertyList Properties {get;}

public:

new property PCTLoopFunctionPropertyList^ Properties {

   PCTLoopFunctionPropertyList^ get();

}


Example

**C#**

```
Function func;

func.Properties[Properties.Function.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.Function.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.Function.FUNC_DEVICETAG_FULL];
```
