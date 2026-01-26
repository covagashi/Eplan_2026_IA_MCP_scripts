# VerifyInstallationSpace(IEnumerable<InstallationSpace>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyInstallationSpace(IEnumerable{InstallationSpace}).html

---

Starts a check run for the given installation spaces.

Syntax

**C#**



public void VerifyInstallationSpace( 

   IEnumerable<InstallationSpace> colInstallationSpaces

)

public:

void VerifyInstallationSpace( 

   IEnumerable<InstallationSpace^>^ colInstallationSpaces

)


#### Parameters

*colInstallationSpaces*
:   List of installation spaces to check.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Throw if parameter is invalid. |
