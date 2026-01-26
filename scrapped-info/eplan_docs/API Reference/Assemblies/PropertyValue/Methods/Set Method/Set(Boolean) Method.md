# Set(Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Set(Boolean).html

---

Sets `int` value in PropertyValue object.

Syntax

**C#**



public PropertyValue Set( 

   bool b

)

public:

PropertyValue^ Set( 

   bool b

)


#### Parameters

*b*
:   bool to convert

#### Return Value

This object is returned.

Remarks

In case this `PropertyValue` object was create by user only the local value of this object will be change/set.

If this `PropertyValue` object was accrued from property list or from `StorableObject` then also value in original location will be changed.
