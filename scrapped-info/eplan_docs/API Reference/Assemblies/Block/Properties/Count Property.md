# Count Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block~Count.html

---

Number of objects in the block.

Syntax

**C#**



public int Count {get;}

public:

property int Count {

   int get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when operation get has failed. |

Remarks

This field shows the number of objects included in the block. A `SymbolReference` object, even if it's a part of the block, is not included.
