# ToDisplay Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser~ToDisplay.html

---

Convert the value to a new unit (of parameterForConversion) of this group and make a display string out of it.

Syntax

**C#**



public string ToDisplay( 

   ParserParameter parameterForConversion

)

public:

String^ ToDisplay( 

   ParserParameter^ parameterForConversion

)


#### Parameters

*parameterForConversion*
:   the parameters used for the conversion

#### Return Value

Returns the new display string

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | The value of the parameter object is NULL. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The unit group of parameterForConversion and me differs |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The function Set was not called and no parameters are available. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The Conversion failed. |
