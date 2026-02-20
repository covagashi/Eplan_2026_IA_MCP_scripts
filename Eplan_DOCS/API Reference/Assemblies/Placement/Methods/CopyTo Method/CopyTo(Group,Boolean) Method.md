# CopyTo(Group,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~CopyTo(Group,Boolean).html

---

Copy Placement and insert the Copy into destination group. Copied placement will be inserted into desired project of destination group. If this placement is temporary, the copy will be persistent, if the destination group is also persistent. Group or Page, where the placement will be inserted. Defines whether a layer should be matched by name.

Syntax

**C#**



public Placement CopyTo( 

   Group destinationGroup,

   bool bMatchLayerNames

)

public:

Placement^ CopyTo( 

   Group^ destinationGroup,

   bool bMatchLayerNames

)


#### Parameters

*destinationGroup*
:   Group or Page, where the placement will be inserted.

*bMatchLayerNames*
:   Defines whether a layer should be matched by name.
