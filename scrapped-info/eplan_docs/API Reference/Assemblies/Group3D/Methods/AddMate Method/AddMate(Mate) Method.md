# AddMate(Mate) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Group3D~AddMate(Mate).html

---

Adds a mate to a group

Syntax

**C#**



public void AddMate( 

   Mate customMate

)

public:

void AddMate( 

   Mate^ customMate

)


#### Parameters

*customMate*

Remarks

Adds a mate to a group. Source object is taken from a custom mate (if exists), otherwise it is a first subplacement of a group.
