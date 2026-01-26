# GetHttpClient Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~GetHttpClient.html

---

Gets HttpClient object. IHttpClientFactory is used internally to create the HttpClient object.

Syntax

**C#**



IdentityClientResponse GetHttpClient( 

   string strClientId,

   string url,

   ref HttpClient httpClient

)

IdentityClientResponse^ GetHttpClient( 

   String^ strClientId,

   String^ url,

   HttpClient^% httpClient

)


#### Parameters

*strClientId*
:   ClientId name.

*url*
:   URL for which a proxy object will be created and set in the HttpClient object.

*httpClient*
:   Valid HttpClient object if success, otherwise null.

#### Return Value

IdentityClientResponse: operation result.

Remarks

A proxy for the baseAddress and the authorization header to access the Eplan Cloud service (strClientId) are set by default in the returned HttpClient object. In this way it is ready for use.
