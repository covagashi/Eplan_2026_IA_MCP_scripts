# AddSupportBarPosition Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddSupportBarPosition.html

---

Add a new support bar position to the part. That position is added to the end of the support bar position list.

Syntax

**C#**



public MDPartSupportBarPosition AddSupportBarPosition()

public:

MDPartSupportBarPosition^ AddSupportBarPosition();


Remarks

The part has to have set product top group: mechanic, product group: busbar and product sub group: busbar adapter to be able to store support bar area positions.
