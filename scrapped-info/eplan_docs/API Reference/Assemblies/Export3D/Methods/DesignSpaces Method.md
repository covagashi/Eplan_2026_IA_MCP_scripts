# DesignSpaces Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export3D~DesignSpaces.html

---

Exports components of design space as xml and step data.

Syntax

**C#**



public bool DesignSpaces( 

   Project oProject,

   string strTargetDirectory,

   bool bEntireProject,

   IEnumerable<InstallationSpace> listInstallationSpaces,

   string strScheme

)

public:

bool DesignSpaces( 

   Project^ oProject,

   String^ strTargetDirectory,

   bool bEntireProject,

   IEnumerable<InstallationSpace^>^ listInstallationSpaces,

   String^ strScheme

)


#### Parameters

*oProject*
:   Project to be exported. Can not be `null`.

*strTargetDirectory*
:   Directory to which files will be written. If the folder does not exist, it will be created. If the user does not have the necessary rights to access the file system, an exception will be thrown. Can not be `null` or empty.

*bEntireProject*
:   If true then all project is exported.

*listInstallationSpaces*
:   Collection of installation spaces which will be exported. Can be null if `bEntireProject`

*strScheme*
:   Scheme used to export installation spaces.

#### Return Value

`true` if export finished with success, otherwise `false`

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ArgumentNullException](#) | Thrown when neccessary argument is `null`. |
| [System.ApplicationException](#) | The internal interface used for export could not be created. |
| [System.UnauthorizedAccessException](#) | No user rights to create files on the file system. |

Remarks

Function creates step files and a XML-files with assembling data and numerical control data in path passed by parameter `strTargetDirectory`. Source of this data is whole project or collections of installation spaces. If parameter `bEntireProject` is `true` then `listInstallationSpaces` can be `null`.
