# Equality Operator

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~op_Equality.html

---

Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project.

Syntax

**C#**



public bool operator ==( 

   StorableObject left,

   StorableObject right

)

public:

bool operator ==( 

   StorableObject^ left,

   StorableObject^ right

)


#### Parameters

*left*
:   StorableObject to compare

*right*
:   StorableObject to compare

#### Return Value

true : Both objects are representing the same object in the project

false : Objects are representing different objects in the project
