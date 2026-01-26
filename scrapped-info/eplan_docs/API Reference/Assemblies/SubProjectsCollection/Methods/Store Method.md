# Store Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.SubProjectsCollection~Store.html

---

Inserts filed-off subproject back into the project.

Syntax

**C#**



public void Store( 

   SubProject pSubProject

)

public:

void Store( 

   SubProject^ pSubProject

)


#### Parameters

*pSubProject*

Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown if subproject is in incorrect state and import is not possible. |
| [System.ArgumentNullException](#) | Thrown when parameter is null. |

Remarks

Subproject can be imported only if SubProject.IsStorePossible is `true`.
