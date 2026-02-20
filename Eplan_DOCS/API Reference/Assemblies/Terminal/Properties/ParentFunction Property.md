# ParentFunction Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal~ParentFunction.html

---

Gets parent function (a main function having the same identifying name or, in case of sub-terminals, the main terminal of a multi-level terminal). For main functions it returns NULL.

Syntax

**C#**



public override Function ParentFunction {get;}

public:

property Function^ ParentFunction {

   Function^ get() override;

}


#### Property Value

The parent function

`Null` when the Function object is a main function

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal query for functions throws exception |

Remarks

Note: Accessing this property may be time consuming in case of non-main terminals existing on large terminal strips. Consider usage of the [Terminal.TerminalStripCache](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+TerminalStripCache.html) object when accessing this property multiple times on terminals of the same strip.
