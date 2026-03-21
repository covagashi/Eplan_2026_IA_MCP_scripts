# GetAccessToken Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~GetAccessToken.html

---

Gets access token for a ClientId.

Syntax

**C#**



IdentityClientResponse GetAccessToken( 

   string strClientId

)

IdentityClientResponse^ GetAccessToken( 

   String^ strClientId

)


#### Parameters

*strClientId*
:   ClientId name.

#### Return Value

IdentityClientResponse: operation result.

Remarks

Method called also internally by GetHttpClient() method.
