# Inequality Operator

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~op_Inequality.html

---

.NET operator for comparing two PinBase objects.

Syntax

**C#**



public bool operator !=( 

   PinBase left,

   PinBase right

)

public:

bool operator !=( 

   PinBase^ left,

   PinBase^ right

)


#### Parameters

*left*


*right*

Remarks

Two PinBase objects representing logical conn. points are equal, if they belong to the same parent and they have the same index. In case of PinBase objects which represent graphical conn. points, only indexes are compared (since the Parent property returns NULL).
