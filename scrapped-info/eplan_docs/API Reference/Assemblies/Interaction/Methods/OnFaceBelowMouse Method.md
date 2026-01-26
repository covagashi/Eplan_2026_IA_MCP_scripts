# OnFaceBelowMouse Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnFaceBelowMouse.html

---

Is called after face was found below the mouse pointer.

Syntax

**C#**



public virtual RequestCode OnFaceBelowMouse( 

   ref bool bFound,

   PointD3D[] arrPoints,

   Vector3D vecDirection,

   StorableObject oStorableObject,

   int iDetailId

)

public:

virtual RequestCode OnFaceBelowMouse( 

   bool% bFound,

   array<PointD3D>^ arrPoints,

   Vector3D vecDirection,

   StorableObject^ oStorableObject,

   int iDetailId

)


#### Parameters

*bFound*
:   If set to `true` edge will be highlighted or used in selection.

*arrPoints*


*vecDirection*


*oStorableObject*
:   StorableObject which has been selected.

*iDetailId*

#### Return Value

Default [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html) for this function is `Nothing`.
