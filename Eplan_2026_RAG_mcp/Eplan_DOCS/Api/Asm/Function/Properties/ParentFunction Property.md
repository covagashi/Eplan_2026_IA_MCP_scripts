# ParentFunction Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~ParentFunction.html

---

Gets parent function (a main function having the same identifying name or, in case of sub-terminals, the main terminal of a multi-level terminal). For main functions it returns NULL.

Syntax

**C#**



public virtual Function ParentFunction {get;}

public:

virtual property Function^ ParentFunction {

   Function^ get();

}


#### Property Value

The parent function

`Null` when the Function object is a main function

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal query for functions throws exception |
