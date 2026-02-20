# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager_methods.html

---

For a list of all members of this type, see [ProjectManager members](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CanOpenReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~CanOpenReadOnly.html) | Checks if project can be opened for read-only access without data upgrade. |
| Public Method | [CopyProject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~CopyProject.html) | Copies project. |
| Public Method | [CreateProject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~CreateProject.html) | Create project with given name. |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~Dispose().html) | Virtual deterministic destructor. |
| Public Method | [ExistsProject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~ExistsProject.html) | Check if project placed on given path exist. |
| Public Method | [GetCurrentProjectWithDialog](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~GetCurrentProjectWithDialog.html) | Gets current project. If there are more than one project open, then displays a dialog to let user choose a current one. |
| Public Method | [GetProject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~GetProject.html) | Gets an already open project. |
| Public Method | [GetProjectByObjectId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~GetProjectByObjectId.html) | Gets the project of an object id string. This is the project the object belongs to. |
| Public Method | [GetProjectDatabaseVersion](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~GetProjectDatabaseVersion.html) | Project database version. |
| Public Method | [GetProjectDataCompatibility](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~GetProjectDataCompatibility.html) | Compares database schemes from current and given project. In the result of this check project could ok , need upgrade or just be incompatible. |
| Public Method | [OpenProject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~OpenProject.html) | Overloaded. Opens a project in the requested mode if possible. |
| Public Method | [RemoveProject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~RemoveProject.html) | Removes project |
| Public Method | [UpgradeProjectDatabase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~UpgradeProjectDatabase.html) | Overloaded. Upgrades project. You can check if project need to be upgrade by GetProjectDataCompatibility. Method makes a copy of old project and sets name to (OldProjectName)(V2).(extension). |


