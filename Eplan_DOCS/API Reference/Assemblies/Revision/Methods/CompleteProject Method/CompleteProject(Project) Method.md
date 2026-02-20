# CompleteProject(Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~CompleteProject(Project).html

---

Completes current revision of a project. Used for change tracking.

Syntax

**C#**



public void CompleteProject( 

   Project oProjectToComplete

)

public:

void CompleteProject( 

   Project^ oProjectToComplete

)


#### Parameters

*oProjectToComplete*
:   A project to complete.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the action. |

Remarks

Used for change tracking. When a revision for a project section is active, only the pages and installation spaces of this project section are protected. The project itself stays writable. Otherwise the project is converted to a read-only revision project.
