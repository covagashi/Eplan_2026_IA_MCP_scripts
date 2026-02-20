# IsTransient Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html

---

Determines if the the StorableObject is transient.

The StorableObject is transient when it was created by default constructor and:

it is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),

it is a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html).

Syntax

**C#**



public bool IsTransient {get;}

public:

property bool IsTransient {

   bool get();

}


#### Property Value

true : the StorableObject is transient

false : the StorableObject is a real object in a real project
