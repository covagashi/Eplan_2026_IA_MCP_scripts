# AccessoryLists Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AccessoryLists.html

---

Gets all accessory lists that are stored in the parts database. They are sorted by it's name.

Syntax

**C#**



public MDAccessoryList[] AccessoryLists {get;}

public:

property array<MDAccessoryList^>^ AccessoryLists {

   array<MDAccessoryList^>^ get();

}


Remarks

the accessory lists are sorted by it's name
