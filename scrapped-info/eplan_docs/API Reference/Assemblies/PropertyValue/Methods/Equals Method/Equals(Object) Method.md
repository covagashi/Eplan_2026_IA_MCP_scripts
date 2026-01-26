# Equals(Object) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Equals(Object).html

---

Determines whether the specified object is equal to the current object.

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
:   The object to compare with the current object.

#### Return Value

**true** if the specified object is equal to the current object; otherwise, **false**.

Remarks

If member IsEmpty of compared property value is true then an empty string is used as a value for comparison.
