# VerifyProject(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyProject(String).html

---

Starts a check run for the given project.

Syntax

**C#**



public void VerifyProject( 

   string strFullLinkFileName

)

public:

void VerifyProject( 

   String^ strFullLinkFileName

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project to check.

Exceptions

| Exception | Description |
| --- | --- |
| **InvalidScheme** | An error occurred when used scheme name doesn't exist |
