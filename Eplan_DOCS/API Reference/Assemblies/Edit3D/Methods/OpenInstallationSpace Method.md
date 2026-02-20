# OpenInstallationSpace Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit3D~OpenInstallationSpace.html

---

Opens Installations space with the name passed to strName.

Syntax

**C#**



public InstallationSpace OpenInstallationSpace( 

   string strFullLinkFileName,

   string strFullName

)

public:

InstallationSpace^ OpenInstallationSpace( 

   String^ strFullLinkFileName,

   String^ strFullName

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project.

*strFullName*
:   Full name of the Installation Space. It is visible in property INSTALLATIONSPACE\_FULLNAME.

#### Return Value

The opened InstallationSpace object.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Is thrown in case of invalid \parameters. |
| **ApplicationException** | The graphics editor interface could not be created. |
