# AddLockedMountingAreaPosition Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddLockedMountingAreaPosition.html

---

Add a new locked mounting area position to the part. That position is added to the end of the locked mounting area position list.

Syntax

**C#**



public MDPartLockedMountingAreaPosition AddLockedMountingAreaPosition()

public:

MDPartLockedMountingAreaPosition^ AddLockedMountingAreaPosition();


Remarks

The part has to have product top group: mechanic and product group: housing to be able to store locked mounting area positions.
