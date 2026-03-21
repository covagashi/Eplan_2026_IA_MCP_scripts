# All Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ViewPart+PropertyPlacementsSchemasList~All.html

---

Returns an array of SymbolReference::PropertyPlacementsSchema elements representing predefined property placements configurations for the symbol. Each of the predefined configuration is represented by a name visible in the GUI and an ID that may be used to select a specific configuration.

Syntax

**C#**



public ViewPart.PropertyPlacementsSchema[] All {get;}

public:

property array<ViewPart.PropertyPlacementsSchema^>^ All {

   array<ViewPart.PropertyPlacementsSchema^>^ get();

}

