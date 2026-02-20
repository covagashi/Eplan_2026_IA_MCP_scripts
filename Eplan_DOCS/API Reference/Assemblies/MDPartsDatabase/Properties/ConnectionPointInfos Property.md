# ConnectionPointInfos Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ConnectionPointInfos.html

---

Gets all connection point infos that are stored in the parts database.

Syntax

**C#**



public MDConnectionPointInfo[] ConnectionPointInfos {get;}

public:

property array<MDConnectionPointInfo^>^ ConnectionPointInfos {

   array<MDConnectionPointInfo^>^ get();

}


Remarks

The connection point infos are sorted by it's name
