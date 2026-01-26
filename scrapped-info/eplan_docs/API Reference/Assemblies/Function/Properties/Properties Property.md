# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~Properties.html

---

EPLAN properties of the Function object.

Syntax

**C#**



public new FunctionPropertyList Properties {get;}

public:

new property FunctionPropertyList^ Properties {

   FunctionPropertyList^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) | Thrown when this property is used for [Eplan.EplApi.DataModel.EObjects.TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html) or [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html) objects |

Remarks

Do NOT use this function for `TerminalStrip` and `PlugStrip` objects. Those classes have their own 'Properties' members which hide the 'Properties' member of the Function class. When getting/setting the FUNC\_CONNECTIONDESIGNATION, FUNC\_CONNECTIONDESCRIPTION and FUNC\_CONNECTIONCROSSSECTIONS properties, note that the maximum index which can be used is not only determined by the maximum index defined in the properties' definitions but also depends on the count of the function's connection points (i.e. cannot be higher than that).

Example

**C#**

```
Function func;

func.Properties[Properties.Function.DESIGNATION_PLANT] = "AP";

func.Properties[Properties.Function.FUNC_COMMENT] = "that is a good function";

string s = func.Properties[Properties.Function.FUNC_DEVICETAG_FULL];
```
