# VerifyMDPartsDatabaseItems(IEnumerable<MDPartsDatabaseItem>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Check~VerifyMDPartsDatabaseItems(IEnumerable{MDPartsDatabaseItem}).html

---

Starts a check run for the given MDPartsDatabaseItems (MDParts).

Syntax

**C#**



public void VerifyMDPartsDatabaseItems( 

   IEnumerable<MDPartsDatabaseItem> oItems

)

public:

void VerifyMDPartsDatabaseItems( 

   IEnumerable<MDPartsDatabaseItem^>^ oItems

)


#### Parameters

*oItems*
:   Parts collection.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Throw if parameter is invalid. |

Remarks

Last-used scheme will be used which is currently set in GUI.
