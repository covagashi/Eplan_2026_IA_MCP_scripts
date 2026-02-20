# AssignConfigurablePropertiesScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AssignConfigurablePropertiesScheme.html

---

Assigns given configurable properties scheme to the part.

Syntax

**C#**



public void AssignConfigurablePropertiesScheme( 

   string strSchemeName

)

public:

void AssignConfigurablePropertiesScheme( 

   String^ strSchemeName

)


#### Parameters

*strSchemeName*
:   Configurable properties scheme name.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown if `strSchemeName` is `null` or empty. |
|  | Thrown if scheme from `strSchemeName` does not exist. |

Remarks

When properties which are in scheme are not configured scheme will not be set.
