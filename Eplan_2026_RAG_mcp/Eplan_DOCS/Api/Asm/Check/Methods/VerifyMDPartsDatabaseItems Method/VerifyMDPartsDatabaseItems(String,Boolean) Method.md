# VerifyMDPartsDatabaseItems(String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyMDPartsDatabaseItems(String,Boolean).html

---

Starts a check run for all MDParts or only for MDPartsDatabaseMessages marked as done depending on bVerifyCompletedMessagesOnly parameter.

Syntax

**C#**



public void VerifyMDPartsDatabaseItems( 

   string strVerificationScheme,

   bool bVerifyCompletedMessagesOnly

)

public:

void VerifyMDPartsDatabaseItems( 

   String^ strVerificationScheme,

   bool bVerifyCompletedMessagesOnly

)


#### Parameters

*strVerificationScheme*
:   Scheme to use for the check run.

*bVerifyCompletedMessagesOnly*
:   Verifies completed messages only when true

Exceptions

| Exception | Description |
| --- | --- |
| **InvalidScheme** | An error occurred when used scheme name doesn't exist |
| [System.ArgumentNullException](#) | Throw if parameter is invalid. |

Remarks

If the scheme name is empty, the last-used scheme will be used which is currently set in GUI.
