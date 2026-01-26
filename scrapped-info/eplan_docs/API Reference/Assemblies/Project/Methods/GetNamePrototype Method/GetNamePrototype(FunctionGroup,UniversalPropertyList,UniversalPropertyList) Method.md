# GetNamePrototype(FunctionGroup,UniversalPropertyList,UniversalPropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic427.html

---

Gets the name prototype for a given function group. For given function group two separate lists with properties used in project structure are created.

Syntax

**C#**



public bool GetNamePrototype( 

   Project.FunctionGroup eFgr,

   UniversalPropertyList describing,

   UniversalPropertyList identifying

)

public:

bool GetNamePrototype( 

   Project.FunctionGroup eFgr,

   UniversalPropertyList^ describing,

   UniversalPropertyList^ identifying

)


#### Parameters

*eFgr*
:   Function group

*describing*
:   Property list - filled with Describing properties

*identifying*
:   Property list - filled with Identifying properties

#### Return Value

True when properties for both lists were found
