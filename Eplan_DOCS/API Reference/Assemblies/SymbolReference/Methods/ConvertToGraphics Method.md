# ConvertToGraphics Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~ConvertToGraphics.html

---

Converts the symbol representing this object into a group of graphical placements.

Syntax

**C#**



public Group ConvertToGraphics()

public:

Group^ ConvertToGraphics();


#### Return Value

A Group of graphical placements that the symbol is converted into.

Exceptions

| Exception | Description |
| --- | --- |
| [System.NotImplementedException](#) | Thrown when the internal interface is not accessible and the conversion cannot be executed. |
| [DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when this object is not placed. |

Remarks

Note: After successful conversion this object is not valid anymore.
