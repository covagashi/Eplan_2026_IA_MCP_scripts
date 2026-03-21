# LoadDirectory Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~LoadDirectory.html

---

Scans directory for projects to add them into the project management.

Syntax

**C#**



public void LoadDirectory( 

   string strProjectsDirectory,

   bool bWithSubDirs

)

public:

void LoadDirectory( 

   String^ strProjectsDirectory,

   bool bWithSubDirs

)


#### Parameters

*strProjectsDirectory*
:   Path to directory which will be scanned. If `null` or `empty` then default path is used.

*bWithSubDirs*
:   Determines whether sub directories are also scanned for projects.

Exceptions

| Exception | Description |
| --- | --- |
| [System.IO.DirectoryNotFoundException](#) | Thrown if directory is not `null` or `empty` and does not exists. |
| [System.ApplicationException](#) | Thrown if the functionality is not available. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while executing the method. |

Remarks

To access existing projects from the project management, they must be loaded into the project management. This method allows user to search for projects in directories under given path. If no path is passed then method uses default value which is stored in setting 'USER.TrDMProject.Masterdata.Pathnames.Projects'.
