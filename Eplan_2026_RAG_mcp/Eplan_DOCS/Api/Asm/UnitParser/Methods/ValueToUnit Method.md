# ValueToUnit Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser~ValueToUnit.html

---

Convert the value to a new unit (of parameterForConversion) of this group.

Syntax

**C#**



public double ValueToUnit( 

   ParserParameter parameterForConversion

)

public:

double ValueToUnit( 

   ParserParameter^ parameterForConversion

)


#### Parameters

*parameterForConversion*
:   the parameters used for the conversion

#### Return Value

Returns the calculated number

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | The value of the parameter object is NULL. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The unit group of parameterForConversion and me differs |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The function Set was not called and no parameters are available. |
