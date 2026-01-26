# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Location~Create.html

---

Creates location in the given hierarchy with a given sort order.

Syntax

**C#**



public bool Create( 

   Project oProject,

   Project.Hierarchy eHierarchy,

   string strProps,

   Project.LocationSortOrder eSort

)

public:

bool Create( 

   Project^ oProject,

   Project.Hierarchy eHierarchy,

   String^ strProps,

   Project.LocationSortOrder eSort

)


#### Parameters

*oProject*
:   [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) where the location will be created.

*eHierarchy*
:   Hierarchy identifier

*strProps*
:   Location name

*eSort*
:   Sort order - determines the position of created location.

#### Return Value

True if location was created
