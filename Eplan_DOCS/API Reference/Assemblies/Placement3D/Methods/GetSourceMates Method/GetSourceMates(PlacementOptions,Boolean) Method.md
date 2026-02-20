# GetSourceMates(PlacementOptions,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetSourceMates(PlacementOptions,Boolean).html

---

Get array of all source mates from this object. Placement optionsConsider child mounting surfaces

Syntax

**C#**



public PointMate[] GetSourceMates( 

   Mate.Enums.PlacementOptions ePlacementOptions,

   bool bConsiderMountingSurfaces

)

public:

array<PointMate^>^ GetSourceMates( 

   Mate.Enums.PlacementOptions ePlacementOptions,

   bool bConsiderMountingSurfaces

)


#### Parameters

*ePlacementOptions*
:   Placement options

*bConsiderMountingSurfaces*
:   Consider child mounting surfaces
