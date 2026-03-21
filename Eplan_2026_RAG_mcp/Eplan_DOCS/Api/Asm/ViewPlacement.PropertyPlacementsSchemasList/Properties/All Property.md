# All Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacement+PropertyPlacementsSchemasList~All.html

---

Returns an array of ViewPlacement::PropertyPlacementsSchema elements representing predefined property placements configurations for the symbol. Each of the predefined configuration is represented by a name visible in the GUI and an ID that may be used to select a specific configuration.

Syntax

**C#**



public ViewPlacement.PropertyPlacementsSchema[] All {get;}

public:

property array<ViewPlacement.PropertyPlacementsSchema^>^ All {

   array<ViewPlacement.PropertyPlacementsSchema^>^ get();

}

