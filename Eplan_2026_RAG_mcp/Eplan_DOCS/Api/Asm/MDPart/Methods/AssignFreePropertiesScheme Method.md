# AssignFreePropertiesScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AssignFreePropertiesScheme.html

---

Assigns given free properties scheme to the part.

Syntax

**C#**



public void AssignFreePropertiesScheme( 

   string strSchemeName

)

public:

void AssignFreePropertiesScheme( 

   String^ strSchemeName

)


#### Parameters

*strSchemeName*
:   Free properties scheme name.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown if `strSchemeName` is `null` or empty. |
|  | Thrown if scheme from `strSchemeName` does not exist. |
