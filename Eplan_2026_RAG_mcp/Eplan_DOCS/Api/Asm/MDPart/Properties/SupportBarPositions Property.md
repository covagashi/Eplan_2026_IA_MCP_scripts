# SupportBarPositions Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~SupportBarPositions.html

---

Get all support bar area positions of the part.

Syntax

**C#**



public MDPartSupportBarPosition[] SupportBarPositions {get;}

public:

property array<MDPartSupportBarPosition^>^ SupportBarPositions {

   array<MDPartSupportBarPosition^>^ get();

}


Remarks

The part has to have set product top group: mechanic, product group: busbar and product sub group: busbar adapter to be able to store support bar area positions.
