# Set(Double,String,ParserParameter) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.UnitParser~Set(Double,String,ParserParameter).html

---

The start of any parse. Set the number and the unit to parse and fill the unit of this text in the parser parameters.

Syntax

**C#**



public void Set( 

   double dValue,

   string strUnitName,

   ParserParameter parameter

)

public:

void Set( 

   double dValue,

   String^ strUnitName,

   ParserParameter^ parameter

)


#### Parameters

*dValue*
:   the number

*strUnitName*
:   the unit as string

*parameter*
:   the parameters with the unit of this string. Afterwards the unit group is defined for the unit parser.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | The value of the parameter object is NULL. |
