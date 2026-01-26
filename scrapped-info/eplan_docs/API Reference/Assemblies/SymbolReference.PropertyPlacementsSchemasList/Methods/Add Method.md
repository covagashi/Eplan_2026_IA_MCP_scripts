# Add Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+PropertyPlacementsSchemasList~Add.html

---

Adds or saves element representing property placements configuration for the symbol. This also sets the current property placements configuration of the symbol.

Syntax

**C#**



public SymbolReference.PropertyPlacementsSchema Add( 

   string sConfigurationName

)

public:

SymbolReference.PropertyPlacementsSchema^ Add( 

   String^ sConfigurationName

)


#### Parameters

*sConfigurationName*

Remarks

This function currently does not deletes the existing property placements. This functionality in previews versions has resulted in inconsistent behavior compared with GUI.
