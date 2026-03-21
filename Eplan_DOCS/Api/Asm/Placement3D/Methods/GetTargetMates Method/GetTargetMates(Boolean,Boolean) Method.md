# GetTargetMates(Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetTargetMates(Boolean,Boolean).html

---

Get array of all target mates from this object. Consider mounting clearanceConsider child mounting surfaces

Syntax

**C#**



public Mate[] GetTargetMates( 

   bool bConsiderMountingClearance,

   bool bConsiderMountingSurfaces

)

public:

array<Mate^>^ GetTargetMates( 

   bool bConsiderMountingClearance,

   bool bConsiderMountingSurfaces

)


#### Parameters

*bConsiderMountingClearance*
:   Consider mounting clearance

*bConsiderMountingSurfaces*
:   Consider child mounting surfaces
