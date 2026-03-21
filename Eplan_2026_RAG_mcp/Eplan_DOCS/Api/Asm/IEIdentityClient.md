# IEIdentityClient

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient.html

---

Interface for Eplan.IdentityClient.Authentification namespace.

Syntax

**C#**



[NullableContext(1)]

public interface IEIdentityClient

[NullableContext(1)]

public interface class IEIdentityClient

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [Exit](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~Exit.html) | Exits from IdentityClient. |
| Method | [GetAccessToken](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~GetAccessToken.html) | Gets access token for a ClientId. |
| Method | [GetHttpClient](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~GetHttpClient.html) | Gets HttpClient object. IHttpClientFactory is used internally to create the HttpClient object. |
| Method | [GetProxySettings](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~GetProxySettings.html) | Gets custom proxy connection configuration. |
| Method | [GetUserProfile](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~GetUserProfile.html) | Gets Eplan cloud user profile information. |
| Method | [GetUserProfileAsJson](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~GetUserProfileAsJson.html) | Gets Eplan cloud user profile information in a JSON format. |
| Method | [InitIdentityClient](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~InitIdentityClient.html) | Initializes Eplan IdentityClient |
| Method | [IsUserAuthenticated](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~IsUserAuthenticated.html) | Is the current user authenticated |
| Method | [RegisterClientId](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~RegisterClientId.html) | Registers ClientId of an Eplan Cloud service. |
| Method | [SetProductInfo](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~SetProductInfo.html) | Sets product information |
| Method | [SetProxy](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~SetProxy.html) | Sets custom proxy connection configuration. |
| Method | [Signin](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~Signin.html) | Signs in to Eplan Cloud. |
| Method | [Signout](Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~Signout.html) | Signs out from Eplan Cloud. |



Public Events

|  | Name | Description |
| --- | --- | --- |
| Event | [EplanCloudResourceDeprecationEvent](topic1734.html) | Event raised when an Eplan Cloud resource is deprecated |


