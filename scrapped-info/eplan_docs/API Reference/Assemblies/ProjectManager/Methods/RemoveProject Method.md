# RemoveProject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~RemoveProject.html

---

Removes project

Syntax

**C#**



public void RemoveProject( 

   string projectLinkFilePath

)

public:

void RemoveProject( 

   String^ projectLinkFilePath

)


#### Parameters

*projectLinkFilePath*
:   Path to project link file name, for example "C\:\\EplanP8\\Projects\\User\\EPLAN\_Sample\_Project.elk"

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when the source project does not exist |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | \Throws exception when project is read\-only. |
| [System.ArgumentNullException](#) | Thrown when `projectLinkFilePath` is `null`. |
