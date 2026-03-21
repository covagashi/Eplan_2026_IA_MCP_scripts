# Mirror(Placement[],PointD,PointD,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~Mirror(Placement[],PointD,PointD,Boolean).html

---

Mirrors placements

Syntax

**C#**



public void Mirror( 

   Placement[] placements,

   PointD start,

   PointD end,

   bool bCopyObjects

)

public:

void Mirror( 

   array<Placement^>^ placements,

   PointD start,

   PointD end,

   bool bCopyObjects

)


#### Parameters

*placements*
:   Placements to mirror.

*start*
:   Start point of the mirror axis

*end*
:   End point of the mirror axis

*bCopyObjects*
:   Determines if objects are copied or moved to the mirror position

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Is thrown in case of NULL placements |
| [System.ArgumentException](#) | Is thrown in case if start equal to end |

Remarks

Mirror is done without numeration. If necessary, please renumber objects by 'Renumber' class
