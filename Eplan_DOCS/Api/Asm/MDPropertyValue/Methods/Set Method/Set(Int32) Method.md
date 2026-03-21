# Set(Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Set(Int32).html

---

Sets `long` value in MDPropertyValue object.

Syntax

**C#**



public MDPropertyValue Set( 

   int i

)

public:

MDPropertyValue^ Set( 

   int i

)


#### Parameters

*i*
:   `long` to convert

#### Return Value

This object is returned.

Remarks

In case where this `MDPropertyValue` object was created by user only the local value of this object will be change/set.

If this `MDPropertyValue` object was acquired from property list or from `StorableObject` then also value in original location will be changed.
