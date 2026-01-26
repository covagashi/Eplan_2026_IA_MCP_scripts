# RouteConnection Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService3D~RouteConnection.html

---

Creates new route of an existing connection 3d.

Syntax

**C#**



public RoutingSegment[] RouteConnection( 

   Connection3D connection3D,

   RoutingSegment[] preRoutingSegments

)

public:

array<RoutingSegment^>^ RouteConnection( 

   Connection3D^ connection3D,

   array<RoutingSegment^>^ preRoutingSegments

)


#### Parameters

*connection3D*
:   Connection3D being routed

*preRoutingSegments*
:   Pre-set array of segments

#### Return Value

An array of routed segments.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when necessary argument is `null`. |
| [System.ApplicationException](#) | An interface used for export could not be created. |
