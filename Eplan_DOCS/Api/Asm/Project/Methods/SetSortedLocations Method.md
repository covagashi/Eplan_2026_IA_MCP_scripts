# SetSortedLocations Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~SetSortedLocations.html

---

Sets the location order, as in the arrLocations parameter, for given hierarchy type. Locations existing in project and not passed in arrLocations are placed after the passed ones. If arrLocations parameter contains not existing location name, this method returns false and no changes are made to the project

Syntax

**C#**



public bool SetSortedLocations( 

   Project.Hierarchy type,

   string[] arrLocations

)

public:

bool SetSortedLocations( 

   Project.Hierarchy type,

   array<String^>^ arrLocations

)


#### Parameters

*type*
:   Location hierarchy

*arrLocations*
:   List of locations

Remarks

Method throws BaseException when a Project was opened without an exclusive lock.
