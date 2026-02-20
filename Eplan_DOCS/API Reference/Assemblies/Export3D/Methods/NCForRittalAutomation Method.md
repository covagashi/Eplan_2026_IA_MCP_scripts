# NCForRittalAutomation Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export3D~NCForRittalAutomation.html

---

Exports drillings of a 3d objects as numerical control data for Rittal - Perforex BC machine.

Syntax

**C#**



public bool NCForRittalAutomation( 

   Project oProject,

   string strMachineName,

   string strMaterialName,

   string strTargetDirectory,

   bool bEntireProject,

   IEnumerable<Placement3D> oCollection

)

public:

bool NCForRittalAutomation( 

   Project^ oProject,

   String^ strMachineName,

   String^ strMaterialName,

   String^ strTargetDirectory,

   bool bEntireProject,

   IEnumerable<Placement3D^>^ oCollection

)


#### Parameters

*oProject*
:   Project to be exported. Can not be `null`.

*strMachineName*
:   Name of machine which will be used to export. If null or empty then last used in GUI will be used.

*strMaterialName*
:   Name of material on which drilling will be made. If name will be invalid then default material is being used for export.

*strTargetDirectory*
:   Directory to which files will be written. If the folder does not exist, it will be created. If the user does not have the necessary rights to access the file system, an exception will be thrown. Can not be `null` or empty.

*bEntireProject*
:   If true then all project is exported.

*oCollection*
:   Collection of 3d object from whicg drillings will be exported. Can be null if `bEntireProject`

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

Function creates files with numerical control data in path passed by parameter `strTargetDirectory`. Source of this data is whole project or collections of 3d placements. If parameter `bEntireProject` is `true` then `oCollection` ca be `null`. If machine name is passed it must be valid what means that the must scheme with this name must exists as node under name `"COMPANY.NCLog.KieslingScheme.*"`.
