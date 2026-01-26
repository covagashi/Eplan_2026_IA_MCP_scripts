# RouteConnections(Project,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TopologyService~RouteConnections(Project,Boolean).html

---

Routes topology connections between all function with representation type [Eplan.EplApi.DataModel.DocumentTypeManager.DocumentType.Topology](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentTypeManager+DocumentType.html) by existing segments in given project.

Syntax

**C#**



public void RouteConnections( 

   Project pProject,

   bool bShowRoutedConnections

)

public:

void RouteConnections( 

   Project^ pProject,

   bool bShowRoutedConnections

)


#### Parameters

*pProject*
:   [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) which connections will be routed.

*bShowRoutedConnections*
:   If `true` routed connection are shown in the GED.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | If any parameter is `null`. |
| [System.ArgumentException](#) | If any parameter is invalid. |
| [System.ApplicationException](#) | Failed to route connections. Please refer to the error message. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An internal error occurred during routing. Please refer to the error message. |

Remarks

If topology connection has a starting and ending symbol references on a one page, but one or both those [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html) are not connected by segment to existing topology and this connection can be routed over this topology, then a new segments are created to complete the path. New segment is connected to the nearest routing point.

If on one page lie two elements which have a regular connection a topology connection will be created for them.
