# PlaceAsConnectionDefinitionPoint Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~PlaceAsConnectionDefinitionPoint.html

---

Places this connection as a connection def. point on the given schematic page and in the given location. If this is an uncovered connection template and the location points to a connection line on schematic page, the template automatically becomes covered (i.e. connection is created in the project) Note: When uncovered connection template becomes covered, connections on the page are updated which may affect performance. If this method needs to be called repeatedly, use the [DisableConnectionUpdateStep](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DisableConnectionUpdateStep.html) object to make the performance better.

Syntax

**C#**



public void PlaceAsConnectionDefinitionPoint( 

   Page pPage,

   PointD pntLocation

)

public:

void PlaceAsConnectionDefinitionPoint( 

   Page^ pPage,

   PointD pntLocation

)


#### Parameters

*pPage*


*pntLocation*
