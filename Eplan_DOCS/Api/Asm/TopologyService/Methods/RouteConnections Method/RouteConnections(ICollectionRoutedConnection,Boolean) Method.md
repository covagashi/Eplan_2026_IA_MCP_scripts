# RouteConnections(ICollection<RoutedConnection>,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1460.html

---

Routes given topology connections.

Syntax

**C#**



public void RouteConnections( 

   ICollection<RoutedConnection> colConnections,

   bool bShowRoutedConnections

)

public:

void RouteConnections( 

   ICollection<RoutedConnection^>^ colConnections,

   bool bShowRoutedConnections

)


#### Parameters

*colConnections*
:   Collection of topology connections which will be routed. Can't be `null`. Input parameter.

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
