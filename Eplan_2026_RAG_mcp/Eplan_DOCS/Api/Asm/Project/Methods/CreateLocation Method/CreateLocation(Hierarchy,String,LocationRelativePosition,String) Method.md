# CreateLocation(Hierarchy,String,LocationRelativePosition,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic426.html

---

Creates location in the given hierarchy, and places it in position eRelPos relatively to the existing location strRelativeLocation.

Syntax

**C#**



public bool CreateLocation( 

   Project.Hierarchy eHierarchy,

   string strProps,

   Project.LocationRelativePosition eRelPos,

   string strExistingLocation

)

public:

bool CreateLocation( 

   Project.Hierarchy eHierarchy,

   String^ strProps,

   Project.LocationRelativePosition eRelPos,

   String^ strExistingLocation

)


#### Parameters

*eHierarchy*
:   Hierarchy identifier

*strProps*
:   Location name \- properties as string

*eRelPos*
:   Relative position \- determines the position of created location in correspondence to existing location.

*strExistingLocation*
:   Existing location.

#### Return Value

True if location was created.
