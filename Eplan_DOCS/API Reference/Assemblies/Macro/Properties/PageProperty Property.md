# PageProperty Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.Macro~PageProperty.html

---

Gets the property of the n-th page in this macro

Syntax

**C#**



public PropertyValue PageProperty( 

   uint nIndex,

   Properties.Page id,

   int idx

) {get;}

public:

property PropertyValue^ PageProperty {

   PropertyValue^ get(uint nIndex, Properties.Page id, int idx);

}


#### Parameters

*nIndex*
:   the nIndex-th page is get the property from (one based)

*id*
:   the property id

*idx*
:   the property index
