# CopyTo(Group) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~CopyTo(Group).html

---

Copy Placement and insert the Copy into destination group. Copied placement will be inserted into desired project of destination group. If this placement is temporary, the copy will be persistent, if the destination group is also persistent. Group or Page, where the placement will be inserted.

Syntax

**C#**



public Placement CopyTo( 

   Group destinationGroup

)

public:

Placement^ CopyTo( 

   Group^ destinationGroup

)


#### Parameters

*destinationGroup*
:   Group or Page, where the placement will be inserted.
