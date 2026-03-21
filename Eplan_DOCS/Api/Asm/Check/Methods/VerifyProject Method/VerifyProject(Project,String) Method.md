# VerifyProject(Project,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyProject(Project,String).html

---

Starts a check run for the given project.

Syntax

**C#**



public void VerifyProject( 

   Project oProject,

   string strVerificationScheme

)

public:

void VerifyProject( 

   Project^ oProject,

   String^ strVerificationScheme

)


#### Parameters

*oProject*
:   Project to check.

*strVerificationScheme*
:   Scheme to use for the check run.

Remarks

If the scheme name is empty, the last-used scheme will be used which is currently set in GUI.
