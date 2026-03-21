# CreateLocation(Hierarchy,UniversalPropertyList,LocationSortOrder) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic425.html

---

Creates location in the given hierarchy with a given sort order.

Syntax

**C#**



public bool CreateLocation( 

   Project.Hierarchy eHierarchy,

   UniversalPropertyList pProps,

   Project.LocationSortOrder eSort

)

public:

bool CreateLocation( 

   Project.Hierarchy eHierarchy,

   UniversalPropertyList^ pProps,

   Project.LocationSortOrder eSort

)


#### Parameters

*eHierarchy*
:   Hierarchy identifier

*pProps*
:   Location name - list of properties

*eSort*
:   Sort order - determines the position of created location.

#### Return Value

True if location was created
