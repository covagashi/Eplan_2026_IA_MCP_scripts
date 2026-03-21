# RenumberCables(Project,String,Boolean,Boolean,Int32,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1309.html

---

Starts a check run for the given MDPartsDatabaseItems (MDParts).

Syntax

**C#**



public void VerifyMDPartsDatabaseItems( 

   IEnumerable<MDPartsDatabaseItem> oItems,

   string strVerificationScheme

)

public:

void VerifyMDPartsDatabaseItems( 

   IEnumerable<MDPartsDatabaseItem^>^ oItems,

   String^ strVerificationScheme

)


#### Parameters

*oItems*
:   Parts collection.

*strVerificationScheme*
:   Scheme to use for the check run.

Exceptions

| Exception | Description |
| --- | --- |
| **InvalidScheme** | An error occurred when used scheme name doesn't exist |
| [System.ArgumentNullException](#) | Throw if parameter is invalid. |

Remarks

If the scheme name is empty, the last-used scheme will be used which is currently set in GUI.
