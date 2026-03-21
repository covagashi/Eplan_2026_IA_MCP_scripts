# VerifyMDPartsDatabaseItems(Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyMDPartsDatabaseItems(Boolean).html

---

Starts a check run for all MDParts or only for MDPartsDatabaseMessages marked as done depending on bVerifyCompletedMessagesOnly parameter.

Syntax

**C#**



public void VerifyMDPartsDatabaseItems( 

   bool bVerifyCompletedMessagesOnly

)

public:

void VerifyMDPartsDatabaseItems( 

   bool bVerifyCompletedMessagesOnly

)


#### Parameters

*bVerifyCompletedMessagesOnly*
:   Verifies completed messages only when true

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Throw if parameter is invalid. |

Remarks

Last-used scheme will be used which is currently set in GUI.
