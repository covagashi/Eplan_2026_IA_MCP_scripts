# OnVertex Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnVertex.html

---

Is called after vertex of a 3D mesh was selected by user.

Syntax

**C#**



public virtual RequestCode OnVertex( 

   PointD3D pntLocation,

   StorableObject oStorableObject,

   int iDetailId

)

public:

virtual RequestCode OnVertex( 

   PointD3D pntLocation,

   StorableObject^ oStorableObject,

   int iDetailId

)


#### Parameters

*pntLocation*
:   Location of the selected vertex.

*oStorableObject*
:   StorableObject which has been selected.

*iDetailId*

#### Return Value

Default [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html) for this function is `Nothing`.
