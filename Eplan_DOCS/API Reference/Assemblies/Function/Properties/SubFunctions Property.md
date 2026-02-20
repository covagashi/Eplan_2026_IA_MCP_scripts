# SubFunctions Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~SubFunctions.html

---

Returns an array of sub-functions of the given main function. Sub-functions are all functions having the same identifying device tag (property 20005) which are not main (a.k.a. auxiliary functions).

Syntax

**C#**



public Function[] SubFunctions {get;}

public:

property array<Function^>^ SubFunctions {

   array<Function^>^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the internal query throws an exception. |

Remarks

Only main functions can have sub-functions. In case this function is not main, an empty array is returned.
