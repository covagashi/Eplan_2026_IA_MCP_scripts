# Set(Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Set(Double).html

---

Sets `double` value in MDPropertyValue object.

Syntax

**C#**



public MDPropertyValue Set( 

   double d

)

public:

MDPropertyValue^ Set( 

   double d

)


#### Parameters

*d*
:   `double` to convert

#### Return Value

This object is returned.

Remarks

In case where this `MDPropertyValue` object was created by user only the local value of this object will be changed/set.

If this `MDPropertyValue` object was acquired from property list or from `StorableObject` then also value in original location will be changed.
