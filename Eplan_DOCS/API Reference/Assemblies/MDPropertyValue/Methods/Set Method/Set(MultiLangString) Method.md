# Set(MultiLangString) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Set(MultiLangString).html

---

Sets [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html) value in MDPropertyValue object.

Syntax

**C#**



public MDPropertyValue Set( 

   MultiLangString mls

)

public:

MDPropertyValue^ Set( 

   MultiLangString^ mls

)


#### Parameters

*mls*
:   [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html) to convert

#### Return Value

This object is returned.

Remarks

In case where this `MDPropertyValue` object was created by user only the local value of this object will be changed/set.

If this `MDPropertyValue` object was acquired from property list or from `StorableObject` then also value in original location will be changed.
