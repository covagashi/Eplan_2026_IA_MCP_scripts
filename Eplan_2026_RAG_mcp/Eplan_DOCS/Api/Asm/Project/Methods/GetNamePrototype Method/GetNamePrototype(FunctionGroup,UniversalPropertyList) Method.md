# GetNamePrototype(FunctionGroup,UniversalPropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~GetNamePrototype(FunctionGroup,UniversalPropertyList).html

---

Gets the name prototype for a given function group. This function will be used, when it needs to be verified, which properties are the part of the objects' name (e.g. for Pages). As a result property list will be filled with property identifiers and empty values.

Syntax

**C#**



public bool GetNamePrototype( 

   Project.FunctionGroup eFgr,

   UniversalPropertyList pOutPrototype

)

public:

bool GetNamePrototype( 

   Project.FunctionGroup eFgr,

   UniversalPropertyList^ pOutPrototype

)


#### Parameters

*eFgr*
:   Function group

*pOutPrototype*
:   Property list - filled with property identifiers and empty values

#### Return Value

True if name prototype was written to the list
