# UnitParser

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser.html

---

The UnitParser class. Here it is possible to read the unit from a string and convert it in other units (of the same unit group)

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.UnitParser**

Syntax

**C#**



public class UnitParser

public ref class UnitParser


Example

Example of using UnitParser class

**C#**

```
UnitParser oUnitParser = new UnitParser();

ParserParameter oParserParameter = new ParserParameter();

oParserParameter.UnitID = Unit.Length_cm;

//Set value in cm

oUnitParser.Set("200 cm", oParserParameter);

//Get value in mm

ParserParameter oParserParameter_mm = new ParserParameter();

oParserParameter_mm.UnitID = Unit.Length_mm;

double dValue_mm = oUnitParser.ValueToUnit(oParserParameter_mm);

//Get value in m

ParserParameter oParserParameter_m = new ParserParameter();

oParserParameter_m.UnitID = Unit.Length_m;

double dValue_m = oUnitParser.ValueToUnit(oParserParameter_m);

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [UnitParser Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser~_ctor.html) | The Constructor |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser~Dispose().html) | Destructor for deterministic finalization of UnitParser object. |
| Public Method | [GetBaseUnit](Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser~GetBaseUnit.html) | Get the base unit of the parsed result of this unit group. |
| Public Method | [GetBaseValue](Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser~GetBaseValue.html) | Get the value of the parsed result in the base unit of this unit group. |
| Public Method | [GetUnit](Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser~GetUnit.html) | Get the unit of the parsed result. |
| Public Method | [GetValue](Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser~GetValue.html) | Get the value of the parsed result. |
| Public Method | [Set](Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser~Set.html) | Overloaded. The start of any parse. Set the number and the unit to parse and fill the unit of this text in the parser parameters. |
| Public Method | [ToDisplay](Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser~ToDisplay.html) | Convert the value to a new unit (of parameterForConversion) of this group and make a display string out of it. |
| Public Method | [ValueToUnit](Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser~ValueToUnit.html) | Convert the value to a new unit (of parameterForConversion) of this group. |


