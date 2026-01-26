# LockedMountingAreaPositions Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~LockedMountingAreaPositions.html

---

Get all locked mounting area positions of the part.

Syntax

**C#**



public MDPartLockedMountingAreaPosition[] LockedMountingAreaPositions {get;}

public:

property array<MDPartLockedMountingAreaPosition^>^ LockedMountingAreaPositions {

   array<MDPartLockedMountingAreaPosition^>^ get();

}


Remarks

The part has to have set product top group: mechanic and product group: housing to be able to store locked mounting area positions.
