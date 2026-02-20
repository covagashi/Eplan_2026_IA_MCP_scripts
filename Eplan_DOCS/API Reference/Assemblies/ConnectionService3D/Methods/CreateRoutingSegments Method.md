# CreateRoutingSegments Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService3D~CreateRoutingSegments.html

---

Creates routing segments for installation space.

Syntax

**C#**



public void CreateRoutingSegments( 

   InstallationSpace pInstallationSpace

)

public:

void CreateRoutingSegments( 

   InstallationSpace^ pInstallationSpace

)


#### Parameters

*pInstallationSpace*
:   Installation space no which routing segments will be created.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when necessary argument is `null`. |
| [System.ApplicationException](#) | An interface used for export could not be created. |
| [System.UnauthorizedAccessException](#) | No user rights to create files on the file system. |
