# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase~Properties.html

---

.NET Property enabling access to P8 properties of the FunctionBase object.

Syntax

**C#**



public new FunctionBasePropertyList Properties {get;}

public:

new property FunctionBasePropertyList^ Properties {

   FunctionBasePropertyList^ get();

}


#### Property Value

P8 properties of the FunctionBase.

Exceptions

| Exception | Description |
| --- | --- |
| [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) | Thrown when this property is used for [Eplan.EplApi.DataModel.EObjects.TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html) or [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html) objects |

Remarks

Do NOT use this function for `TerminalStrip` and `PlugStrip` objects.

Example

**C#**

```
FunctionBase func;

func.Properties[Properties.FunctionBase.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.FunctionBase.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.FunctionBase.FUNC_DEVICETAG_FULL];
```
