# GetLocationPrototype Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~GetLocationPrototype.html

---

Creates location prototype using property list pProps. Property identifiers that describe location are written to the list.

Syntax

**C#**



public bool GetLocationPrototype( 

   Project.Hierarchy eHierarchy,

   UniversalPropertyList pOutPrototype

)

public:

bool GetLocationPrototype( 

   Project.Hierarchy eHierarchy,

   UniversalPropertyList^ pOutPrototype

)


#### Parameters

*eHierarchy*
:   Hierarchy identifier

*pOutPrototype*
:   Property list - filled with property identifiers and empty value

#### Return Value

True if location prototype was written to the list
