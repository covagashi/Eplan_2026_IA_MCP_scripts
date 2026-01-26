# AccessoryPlacements Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AccessoryPlacements.html

---

Gets all accessory lists that are stored in the parts database. They are sorted by it's name.

Syntax

**C#**



public MDAccessoryPlacement[] AccessoryPlacements {get;}

public:

property array<MDAccessoryPlacement^>^ AccessoryPlacements {

   array<MDAccessoryPlacement^>^ get();

}


Remarks

the accessory lists are sorted by it's name
