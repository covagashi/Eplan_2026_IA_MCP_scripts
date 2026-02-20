# LineUp Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Placement3DService~LineUp.html

---

Lines up together the given children of a mounting rail to the certain target direction.

Syntax

**C#**



public bool LineUp( 

   Placement3D[] arrPlacement3D,

   Placement3DService.AlignmentDirection eAlignmentDirection

)

public:

bool LineUp( 

   array<Placement3D^>^ arrPlacement3D,

   Placement3DService.AlignmentDirection eAlignmentDirection

)


#### Parameters

*arrPlacement3D*
:   List of 3D placements to line up together.

*eAlignmentDirection*
:   Alignment direction.
