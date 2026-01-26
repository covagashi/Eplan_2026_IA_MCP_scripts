# RemovePlacement Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~RemovePlacement.html

---

Removes object and all its children only from layout space.

Syntax

**C#**



public void RemovePlacement()

public:

void RemovePlacement();


Remarks

If placement is placed and could exist unplaced, this method could remove it only from installation space (layout space). For other placements method have no effect.
