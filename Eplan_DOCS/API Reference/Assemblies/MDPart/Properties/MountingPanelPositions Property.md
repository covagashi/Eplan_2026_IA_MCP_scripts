# MountingPanelPositions Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~MountingPanelPositions.html

---

Get all support mounting panel positions of the part.

Syntax

**C#**



public MDPartMountingPanelPosition[] MountingPanelPositions {get;}

public:

property array<MDPartMountingPanelPosition^>^ MountingPanelPositions {

   array<MDPartMountingPanelPosition^>^ get();

}


Remarks

The part has to have set product top group: mechanic and product group: cabinet to be able to store mounting panel positions.
