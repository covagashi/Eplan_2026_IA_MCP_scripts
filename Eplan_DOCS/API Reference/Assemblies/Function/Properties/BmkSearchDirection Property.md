# BmkSearchDirection Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~BmkSearchDirection.html

---

The property gives the search direction of the full device tag, when the visible device tag name is empty.

Syntax

**C#**



public Function.Enums.SearchDirection BmkSearchDirection {get;}

public:

property Function.Enums.SearchDirection BmkSearchDirection {

   Function.Enums.SearchDirection get();

}


#### Property Value

Standard: The search direction is equal like the frame direction (left or Top) Alternative: Is the alternative direction of the frame.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when search direction for this function cannot be read. |
