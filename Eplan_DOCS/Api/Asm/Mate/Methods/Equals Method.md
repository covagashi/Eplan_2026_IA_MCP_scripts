# Equals Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Equals.html

---

Operator of comparison implementation. Checks if two mates have same name and belongs to the same object.

Syntax

**C#**



public override bool Equals( 

   object obj

)

public:

bool Equals( 

   Object^ obj

) override


#### Parameters

*obj*
:   Mate to compare

#### Return Value

true : Both objects are representing the same object

false : Objects are representing different objects or one of them is `null`.
