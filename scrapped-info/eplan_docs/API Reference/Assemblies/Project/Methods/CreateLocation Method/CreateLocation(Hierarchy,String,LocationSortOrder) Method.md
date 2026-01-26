# CreateLocation(Hierarchy,String,LocationSortOrder) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~CreateLocation(Hierarchy,String,LocationSortOrder).html

---

Creates location in the given hierarchy with a given sort order.

Syntax

**C#**



public bool CreateLocation( 

   Project.Hierarchy eHierarchy,

   string strProps,

   Project.LocationSortOrder eSort

)

public:

bool CreateLocation( 

   Project.Hierarchy eHierarchy,

   String^ strProps,

   Project.LocationSortOrder eSort

)


#### Parameters

*eHierarchy*
:   Hierarchy identifier

*strProps*
:   Location name - properties as string

*eSort*
:   Sort order - determines the position of created location.

#### Return Value

True if location was created
