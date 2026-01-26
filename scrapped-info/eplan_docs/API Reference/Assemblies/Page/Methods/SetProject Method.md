# SetProject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~SetProject.html

---

Assigns a page to a given project.

Syntax

**C#**



public void SetProject( 

   Project pProject

)

public:

void SetProject( 

   Project^ pProject

)


#### Parameters

*pProject*
:   A project the page is assigned to.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when pProject is `null`. |
| [InsufficientLicenceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InsufficientLicenceException.html) | Thrown when no new logical page can be added to the project. |

Remarks

The page becomes not transient. If the page was previously assigned to another project, it is removed from old one and assigned to the project given as an argument.
