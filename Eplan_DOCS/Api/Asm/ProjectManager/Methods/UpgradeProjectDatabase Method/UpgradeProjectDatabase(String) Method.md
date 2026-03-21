# UpgradeProjectDatabase(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~UpgradeProjectDatabase(String).html

---

Upgrades project. You can check if project need to be upgrade by GetProjectDataCompatibility. Method makes a copy of old project and sets name to (OldProjectName)(V2).(extension).

Syntax

**C#**



public bool UpgradeProjectDatabase( 

   string projectPath

)

public:

bool UpgradeProjectDatabase( 

   String^ projectPath

)


#### Parameters

*projectPath*
:   Path to .elk project file.

#### Return Value

Function returns value about success.

Exceptions

| Exception | Description |
| --- | --- |
| [ProjectNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectNotFoundException.html) | Thrown when project  `projectPath`  doesn't exist. |
| [System.ArgumentNullException](#) | Thrown when `projectPath` is `null`. |

Remarks

Upgrading project invalidates Project objects having projectPath path.
