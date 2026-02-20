# RegisterClientId Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~RegisterClientId.html

---

Registers ClientId of an Eplan Cloud service.

Syntax

**C#**



IdentityClientResponse RegisterClientId( 

   string strClientId

)

IdentityClientResponse^ RegisterClientId( 

   String^ strClientId

)


#### Parameters

*strClientId*
:   ClientId name.

#### Return Value

IdentityClientResponse: operation result.

Remarks

By calling this method the internal TokenManagement will know about the client and manage access token for it.  
After calling this method, one can utilize the method GetAccessToken or GetHttpClient for the registered client.  
Method called also internally by GetHttpClient() method.
