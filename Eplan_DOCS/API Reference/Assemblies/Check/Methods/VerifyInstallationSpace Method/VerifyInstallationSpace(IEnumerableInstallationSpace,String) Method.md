# VerifyInstallationSpace(IEnumerable<InstallationSpace>,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyInstallationSpace(IEnumerable{InstallationSpace},String).html

---

Starts a check run for the given installation spaces.

Syntax

**C#**



public void VerifyInstallationSpace( 

   IEnumerable<InstallationSpace> colInstallationSpaces,

   string strVerificationScheme

)

public:

void VerifyInstallationSpace( 

   IEnumerable<InstallationSpace^>^ colInstallationSpaces,

   String^ strVerificationScheme

)


#### Parameters

*colInstallationSpaces*
:   List of installation spaces to check.

*strVerificationScheme*
:   Scheme to use for the check run.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.HEServices.Exceptions.InvalidScheme](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Exceptions.InvalidScheme.html) | An error occurred when used scheme name doesn't exist |
| [System.ArgumentNullException](#) | Throw if any parameter is invalid. |

Remarks

If the scheme name is empty, the last-used scheme will be used which is currently set in GUI.
