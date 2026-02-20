# CanOpenReadOnly Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~CanOpenReadOnly.html

---

Checks if project can be opened for read-only access without data upgrade.

Syntax

**C#**



public bool CanOpenReadOnly( 

   string projectPath

)

public:

bool CanOpenReadOnly( 

   String^ projectPath

)


#### Parameters

*projectPath*
:   Path to .elk project file.

#### Return Value

Returns true if project can be opened without conversion.

Exceptions

| Exception | Description |
| --- | --- |
| [ProjectNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectNotFoundException.html) | Thrown when project doesn't exist. |
| [System.ArgumentNullException](#) | Thrown when  `projectPath`  is `null`. |
