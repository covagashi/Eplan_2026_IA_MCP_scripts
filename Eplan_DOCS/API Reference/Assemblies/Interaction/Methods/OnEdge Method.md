# OnEdge Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnEdge.html

---

Is called after edged of a 3D mesh was selected by user.

Syntax

**C#**



public virtual RequestCode OnEdge( 

   PointD3D pntStart,

   PointD3D pntEnd,

   StorableObject oStorableObject,

   int iDetailId

)

public:

virtual RequestCode OnEdge( 

   PointD3D pntStart,

   PointD3D pntEnd,

   StorableObject^ oStorableObject,

   int iDetailId

)


#### Parameters

*pntStart*
:   Beginning of the selected edge.

*pntEnd*
:   End of the selected edge.

*oStorableObject*
:   StorableObject which has been selected.

*iDetailId*

#### Return Value

Default [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html) for this function is `Nothing`.
