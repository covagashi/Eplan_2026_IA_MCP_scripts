# Set(String,ParserParameter) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser~Set(String,ParserParameter).html

---

The start of any parse. Set the text to parse and fill the unit of this text in the parser parameters.

Syntax

**C#**



public void Set( 

   string strValueToParse,

   ParserParameter parameter

)

public:

void Set( 

   String^ strValueToParse,

   ParserParameter^ parameter

)


#### Parameters

*strValueToParse*
:   the string with a number and optional a unit

*parameter*
:   the parameters with the unit of this string. Afterwards the unit group is defined for the unit parser.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | The value of the parameter object is NULL. |
