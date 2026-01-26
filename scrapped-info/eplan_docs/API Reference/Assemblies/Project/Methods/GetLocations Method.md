# GetLocations Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~GetLocations.html

---

Returns array of names of project's location for given hierarchy type (PLANT, LOCATION etc.)

Syntax

**C#**



public string[] GetLocations( 

   Project.Hierarchy type

)

public:

array<String^>^ GetLocations( 

   Project.Hierarchy type

)


#### Parameters

*type*
:   Location hierarchy

#### Return Value

[System.String](#) object.

Example

**C#**

```
string[] strLocations = oProject.GetLocations(Project.Hierarchy.Plant);

Console.WriteLine(" Locations :");

foreach(string loc in strLocations)

Console.WriteLine("  " + loc);

```
