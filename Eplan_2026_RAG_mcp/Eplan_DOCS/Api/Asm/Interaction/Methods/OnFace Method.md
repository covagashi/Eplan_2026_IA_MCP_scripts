# OnFace Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnFace.html

---

Is called after face of a 3D mesh was selected by user.

Syntax

**C#**



public virtual RequestCode OnFace( 

   PointD3D[] arrPoints,

   Vector3D vDirection,

   StorableObject oStorableObject,

   int iDetailId

)

public:

virtual RequestCode OnFace( 

   array<PointD3D>^ arrPoints,

   Vector3D vDirection,

   StorableObject^ oStorableObject,

   int iDetailId

)


#### Parameters

*arrPoints*
:   Vertexes of the selected edge.

*vDirection*


*oStorableObject*
:   StorableObject which has been selected.

*iDetailId*

#### Return Value

Default [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html) for this function is `Nothing`.
