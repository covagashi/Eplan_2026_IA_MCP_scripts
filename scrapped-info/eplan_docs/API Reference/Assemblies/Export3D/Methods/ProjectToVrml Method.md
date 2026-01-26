# ProjectToVrml Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export3D~ProjectToVrml.html

---

Exports all installation spaces from project into files in VRML format.

Syntax

**C#**



public bool ProjectToVrml( 

   Project oProject,

   string strTargetDirectory

)

public:

bool ProjectToVrml( 

   Project^ oProject,

   String^ strTargetDirectory

)


#### Parameters

*oProject*
:   Project to be exported. Can not be `null`.

*strTargetDirectory*
:   Directory to which files will be written. If the folder does not exist, it will be created. If the user does not have the necessary rights to access the file system, an exception will be thrown. Can not be `null` or empty.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when neccessary argument is `null`. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The internal interface used for export could not be created. |

Remarks

Names of files are generated from properties [Eplan.EplApi.DataModel.E3D.InstallationSpacePropertyList.INSTALLATIONSPACE\_FULLNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpacePropertyList~INSTALLATIONSPACE_FULLNAME.html).
