# OnEdgeBelowMouse Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnEdgeBelowMouse.html

---

Is called after edge was found below the mouse pointer.

Syntax

**C#**



public virtual RequestCode OnEdgeBelowMouse( 

   ref bool bFound,

   PointD3D pntStart,

   PointD3D pntEnd,

   StorableObject oStorableObject,

   int iDetailId

)

public:

virtual RequestCode OnEdgeBelowMouse( 

   bool% bFound,

   PointD3D pntStart,

   PointD3D pntEnd,

   StorableObject^ oStorableObject,

   int iDetailId

)


#### Parameters

*bFound*
:   If set to `true` edge will be highlighted or used in selection.

*pntStart*
:   Beginning of selected edge.

*pntEnd*
:   End of selected edge.

*oStorableObject*
:   StorableObject which has been selected.

*iDetailId*

#### Return Value

Default [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html) for this function is `Nothing`.
