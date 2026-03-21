# Set Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.ContextParameterBlock~Set.html

---

Set one object with a name

Syntax

**C#**



public void Set( 

   string strName,

   object strObject

)

public:

void Set( 

   String^ strName,

   Object^ strObject

)


#### Parameters

*strName*
:   the name of this parameter.

*strObject*
:   the object saved in this block.

Remarks

overwrites the existing object when a parameter with this name already exists.
