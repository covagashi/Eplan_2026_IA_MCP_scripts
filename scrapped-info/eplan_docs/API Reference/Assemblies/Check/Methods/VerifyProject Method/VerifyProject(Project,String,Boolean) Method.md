# VerifyProject(Project,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyProject(Project,String,Boolean).html

---

Starts a check run for the given project.

Syntax

**C#**



public void VerifyProject( 

   Project oProject,

   string strVerificationScheme,

   bool bVerifyCompletedMessagesOnly

)

public:

void VerifyProject( 

   Project^ oProject,

   String^ strVerificationScheme,

   bool bVerifyCompletedMessagesOnly

)


#### Parameters

*oProject*
:   Project to check.

*strVerificationScheme*
:   Scheme to use for the check run.

*bVerifyCompletedMessagesOnly*
:   Verifies completed messages only when true

Remarks

If the scheme name is empty, the last-used scheme will be used which is currently set in GUI.
