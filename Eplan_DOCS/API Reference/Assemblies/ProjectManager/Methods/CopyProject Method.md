# CopyProject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~CopyProject.html

---

Copies project.

Syntax

**C#**



public void CopyProject( 

   string srcProjectLinkFile,

   string dstProjectLinkFile,

   ProjectManager.CopyMode mode

)

public:

void CopyProject( 

   String^ srcProjectLinkFile,

   String^ dstProjectLinkFile,

   ProjectManager.CopyMode mode

)


#### Parameters

*srcProjectLinkFile*
:   Source project path

*dstProjectLinkFile*
:   Destination project path

*mode*
:   Copy mode

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `srcProjectLinkFile` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `dstProjectLinkFile` is `null`. |
| [System.ArgumentException](#) | Thrown when the source project does not exist |
| [ProjectCopyException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectCopyException.html) | Thrown when project cannot be copied |
| [ProjectNeedsUpgradeException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectNeedsUpgradeException.html) | Thrown when project `srcProjectLinkFile` has old database structure and needs to be upgraded. |
| [IncompatibleDatabaseException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IncompatibleDatabaseException.html) | Thrown when project `srcProjectLinkFile` has incompatible database structure and we can do nothing about it. |
