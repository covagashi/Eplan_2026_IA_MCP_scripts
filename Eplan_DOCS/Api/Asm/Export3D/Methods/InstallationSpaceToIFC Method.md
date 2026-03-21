# InstallationSpaceToIFC Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Export3D~InstallationSpaceToIFC.html

---

Exports single installation space into file in IFC format under given name.

Syntax

**C#**



public bool InstallationSpaceToIFC( 

   InstallationSpace installationSpace,

   string strTargetDirectory,

   string outputFileName,

   string strScheme

)

public:

bool InstallationSpaceToIFC( 

   InstallationSpace^ installationSpace,

   String^ strTargetDirectory,

   String^ outputFileName,

   String^ strScheme

)


#### Parameters

*installationSpace*
:   Installation space which will be exported. Can not be `null` or empty.

*strTargetDirectory*
:   Directory to which files will be written. If the folder does not exist, it will be created. If the user does not have the necessary rights to access the file system, an exception will be thrown. Can not be `null` or empty.

*outputFileName*
:   Name of the exported file.

*strScheme*
:   Scheme used for export.

#### Return Value

if installationSpace is empty, method returns false

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when necessary argument is `null`. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The internal interface used for export could not be created. |
