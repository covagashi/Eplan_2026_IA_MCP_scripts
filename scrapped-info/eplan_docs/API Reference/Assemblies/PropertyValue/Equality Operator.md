# Equality Operator

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~op_Equality.html

---

Determines whether two PropertyValues objects have the same value.

Syntax

**C#**



public bool operator ==( 

   PropertyValue lhs,

   PropertyValue rhs

)

public:

bool operator ==( 

   PropertyValue^ lhs,

   PropertyValue^ rhs

)


#### Parameters

*lhs*


*rhs*

#### Return Value

True when both values are the same.

Remarks

If member IsEmpty of compared property value is true then an empty string is used for comparison.
