# ProjectManagement

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement.html

---

This class contains methods for some project related tasks, like finding a project by its ID, compressing a project, or importing a ProjectInfo.xml file.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.ProjectManagement**

Syntax

**C#**



public class ProjectManagement

public ref class ProjectManagement

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ProjectManagement Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~_ctor.html) | Default constructor |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ActiveProjectManagementDatabase](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~ActiveProjectManagementDatabase.html) | Returns or sets the type of current project management database. Possible values are DatabaseType.SQL and DatabaseType.EPLAN |
| Public Property | [ProjectManagementDatabase](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~ProjectManagementDatabase.html) | Returns or sets the complete filename of the current projectmanagement database or connection string if SQL connection is selected. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CompressProject](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~CompressProject.html) | Overloaded. Compresses a project. |
| Public Method | [CorrectProjectItems](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~CorrectProjectItems.html) | Overloaded. Corrects project items. |
| Public Method | [CreateDatabase](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~CreateDatabase.html) | Create a new projectmanagement database. |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~Dispose().html) | Destructor |
| Public Method | [DoProjectInspection](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~DoProjectInspection.html) | Overloaded. Compares two projects and writes the results as project messages into the message management. This method corresponds to the following functionality of EPLAN Electric P8: Project / Management, Extras / Verify Project |
| Public Method | [ExportPropertyPlacementsSchemas](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~ExportPropertyPlacementsSchemas.html) | Exports property placements schemes. |
| Public Method | [GetProjectByGUID](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~GetProjectByGUID.html) | Method for searching a project by a given project ID from the project management database. |
| Public Method | [GetProjectCount](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~GetProjectCount.html) |  |
| Public Method | [ImportPropertyPlacementsSchemas](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~ImportPropertyPlacementsSchemas.html) | Imports property placements schemes. |
| Public Method | [LoadDirectory](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~LoadDirectory.html) | Scans directory for projects to add them into the project management. |
| Public Method | [PublishProjectForSmartProduction](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~PublishProjectForSmartProduction.html) | Publishes a project |
| Public Method | [ReadProjectInfo](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~ReadProjectInfo.html) | Overloaded. Loads the ProjectInfo.xml file. and sets project properties accordingly. |
| Public Method | [Reorganize](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~Reorganize.html) | Reorganizes a project |
| Public Method | [SetSQLServerConnectionParameters](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~SetSQLServerConnectionParameters.html) | Sets SQL connection parameters. |
| Public Method | [SynchronizeProjects](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~SynchronizeProjects.html) | Overloaded. Synchronizes all projects data from source project into the target project. |
| Public Method | [UpdateProjectStructureFromSettings](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~UpdateProjectStructureFromSettings.html) | Updates project structure for navigator (GUI) according to the project settings. |


