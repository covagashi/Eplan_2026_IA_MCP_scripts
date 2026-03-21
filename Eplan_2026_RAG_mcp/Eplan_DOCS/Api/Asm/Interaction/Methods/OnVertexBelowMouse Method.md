# OnVertexBelowMouse Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnVertexBelowMouse.html

---

Is called after vertex was found below the mouse pointer.

Syntax

**C#**



public virtual RequestCode OnVertexBelowMouse( 

   ref bool bFound,

   PointD3D pntLocation,

   StorableObject oStorableObject,

   int detailId

)

public:

virtual RequestCode OnVertexBelowMouse( 

   bool% bFound,

   PointD3D pntLocation,

   StorableObject^ oStorableObject,

   int detailId

)


#### Parameters

*bFound*
:   If set to `true` edge will be highlighted or used in selection.

*pntLocation*
:   Location of the selected vertex.

*oStorableObject*
:   StorableObject which has been selected.

*detailId*

#### Return Value

Default [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html) for this function is `Nothing`.
