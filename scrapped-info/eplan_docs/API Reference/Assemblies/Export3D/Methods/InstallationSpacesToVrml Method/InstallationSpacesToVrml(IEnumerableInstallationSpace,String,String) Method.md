# InstallationSpacesToVrml(IEnumerable<InstallationSpace>,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1358.html

---

Exports given installation spaces into files in VRML format.

Syntax

**C#**



public bool InstallationSpacesToVrml( 

   IEnumerable<InstallationSpace> listInstallationSpaces,

   string strTargetDirectory,

   string strScheme

)

public:

bool InstallationSpacesToVrml( 

   IEnumerable<InstallationSpace^>^ listInstallationSpaces,

   String^ strTargetDirectory,

   String^ strScheme

)


#### Parameters

*listInstallationSpaces*
:   Collection of installation spaces which will be exported. Can not be `null` or empty.

*strTargetDirectory*
:   Directory to which files will be written. If the folder does not exist, it will be created. If the user does not have the necessary rights to access the file system, an exception will be thrown. If value is `null` or empty target directory from scheme is used.

*strScheme*
:   Scheme used to export installation spaces.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when necessary argument is `null`. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The internal interface used for export could not be created. |
| [Eplan.EplApi.HEServices.Exceptions.InvalidScheme](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Exceptions.InvalidScheme.html) | Thrown if scheme is invalid. |

Remarks

The names of files are generated from given scheme settings.
