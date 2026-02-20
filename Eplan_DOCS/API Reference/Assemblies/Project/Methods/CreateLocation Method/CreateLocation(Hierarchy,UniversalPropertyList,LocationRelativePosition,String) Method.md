# CreateLocation(Hierarchy,UniversalPropertyList,LocationRelativePosition,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic424.html

---

Creates location in the given hierarchy, and places it in position eRelPos relatively to the existing location strExistingLocation.

Syntax

**C#**



public bool CreateLocation( 

   Project.Hierarchy eHierarchy,

   UniversalPropertyList pProps,

   Project.LocationRelativePosition eRelPos,

   string strExistingLocation

)

public:

bool CreateLocation( 

   Project.Hierarchy eHierarchy,

   UniversalPropertyList^ pProps,

   Project.LocationRelativePosition eRelPos,

   String^ strExistingLocation

)


#### Parameters

*eHierarchy*
:   Hierarchy identifier

*pProps*
:   Location name \- list of properties

*eRelPos*
:   Relative position \- determines the position of created location in correspondence to existing location.

*strExistingLocation*
:   Existing location.

#### Return Value

True if location was created.
