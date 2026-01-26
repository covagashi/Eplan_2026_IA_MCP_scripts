# VerifyProject(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyProject(String,String).html

---

Starts a check run for the given project.

Syntax

**C#**



public void VerifyProject( 

   string strFullLinkFileName,

   string strVerificationScheme

)

public:

void VerifyProject( 

   String^ strFullLinkFileName,

   String^ strVerificationScheme

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project to check.

*strVerificationScheme*
:   Scheme to use for the check run.

Remarks

If the scheme name is empty, the last-used scheme will be used which is currently set in GUI.
