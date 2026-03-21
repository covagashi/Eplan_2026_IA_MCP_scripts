# FileOff Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.SubProjectsCollection~FileOff.html

---

Creates subproject, i.e. file it off from the project.

Syntax

**C#**



public void FileOff( 

   SubProject pSubProject

)

public:

void FileOff( 

   SubProject^ pSubProject

)


#### Parameters

*pSubProject*

Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown if subproject is in incorrect state and export is not possible. |
| [System.ArgumentNullException](#) | Thrown when parameter is null. |

Remarks

Subproject can be exported only if SubProject.IsFileOffPossible is `true`. After calling this method source Project object becomes invalid. Valid Project object can be obtained using ProjectManager::CurrentProject or ProjectManager::OpenedProjects property.
