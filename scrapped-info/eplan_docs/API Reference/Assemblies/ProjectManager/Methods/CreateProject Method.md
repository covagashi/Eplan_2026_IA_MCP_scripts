# CreateProject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~CreateProject.html

---

Create project with given name.

Syntax

**C#**



public Project CreateProject( 

   string projectLinkFilePath,

   string projectTemplateFilePath

)

public:

Project^ CreateProject( 

   String^ projectLinkFilePath,

   String^ projectTemplateFilePath

)


#### Parameters

*projectLinkFilePath*
:   Full project link file path

*projectTemplateFilePath*
:   Full template link file path

#### Return Value

[Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) object.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when filename in `projectLinkFilePath` parameter starts or ends with space character. |
| [ProjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectCreationException.html) | Thrown when project cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `projectLinkFilePath` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `projectTemplateFilePath` is `null`. |
| [ProjectLockingException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectLockingException.html) | Thrown when [LockProjectByDefault](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~LockProjectByDefault.html) is `true` and a project cannot be locked. |

Remarks

The newly created project is opened in exclusive mode. This only applies to the API and does not correspond to the behavior in the GUI.
