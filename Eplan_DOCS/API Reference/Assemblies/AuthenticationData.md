# AuthenticationData

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.IdentityClient.Types~Eplan.IdentityClient.AuthenticationData.html

---

AuthenticationData class contains useful authentication data.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.IdentityClient.IdentityClientResponse](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse.html)  
      **Eplan.IdentityClient.AuthenticationData**

Syntax

**C#**



[NullableContext(1)]

[Nullable(0)]

public class AuthenticationData : IdentityClientResponse

[NullableContext(1)]

[Nullable(0)]

public ref class AuthenticationData : public IdentityClientResponse

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [AuthenticationData Constructor](Eplan.IdentityClient.Types~Eplan.IdentityClient.AuthenticationData~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AccessToken](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse~AccessToken.html) | Access token value. (Inherited from [Eplan.IdentityClient.IdentityClientResponse](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse.html)) |
| Public Property | [AccessTokenExpiration](Eplan.IdentityClient.Types~Eplan.IdentityClient.AuthenticationData~AccessTokenExpiration.html) | Date and time of access token expiration. |
| Public Property | [AuthenticationTime](Eplan.IdentityClient.Types~Eplan.IdentityClient.AuthenticationData~AuthenticationTime.html) | Authentication date and time. |
| Public Property | [ClientId](Eplan.IdentityClient.Types~Eplan.IdentityClient.AuthenticationData~ClientId.html) | Service ClientId name. |
| Public Property | [ConfigurationServiceApiVersion](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse~ConfigurationServiceApiVersion.html) | IdentityClient configuration service API version. (Inherited from [Eplan.IdentityClient.IdentityClientResponse](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse.html)) |
| Public Property | [ConfigurationServiceUrl](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse~ConfigurationServiceUrl.html) | IdentityClient configuration service URL. (Inherited from [Eplan.IdentityClient.IdentityClientResponse](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse.html)) |
| Public Property | [Cookies](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse~Cookies.html) | Cookies. (Inherited from [Eplan.IdentityClient.IdentityClientResponse](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse.html)) |
| Public Property | [DisplayName](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse~DisplayName.html) | DisplayName. (Inherited from [Eplan.IdentityClient.IdentityClientResponse](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse.html)) |
| Public Property | [Email](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse~Email.html) | User Email address. (Inherited from [Eplan.IdentityClient.IdentityClientResponse](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse.html)) |
| Public Property | [Environment](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse~Environment.html) | Environment information. (Inherited from [Eplan.IdentityClient.IdentityClientResponse](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse.html)) |
| Public Property | [Error](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse~Error.html) | Error message. (Inherited from [Eplan.IdentityClient.IdentityClientResponse](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse.html)) |
| Public Property | [GracePeriodStartTime](Eplan.IdentityClient.Types~Eplan.IdentityClient.AuthenticationData~GracePeriodStartTime.html) | Date and time of grace period start. |
| Public Property | [IdentityServiceUrl](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse~IdentityServiceUrl.html) | IdentityClient service URL. (Inherited from [Eplan.IdentityClient.IdentityClientResponse](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse.html)) |
| Public Property | [IdentityToken](Eplan.IdentityClient.Types~Eplan.IdentityClient.AuthenticationData~IdentityToken.html) | IdentityClient token. |
| Public Property | [IsSuccess](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse~IsSuccess.html) | Indicates if IdentityStatusCode is success. (Inherited from [Eplan.IdentityClient.IdentityClientResponse](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse.html)) |
| Public Property | [ManagementServiceUrl](Eplan.IdentityClient.Types~Eplan.IdentityClient.AuthenticationData~ManagementServiceUrl.html) | Management service URL. |
| Public Property | [Message](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse~Message.html) | Message. (Inherited from [Eplan.IdentityClient.IdentityClientResponse](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse.html)) |
| Public Property | [OrganizationId](Eplan.IdentityClient.Types~Eplan.IdentityClient.AuthenticationData~OrganizationId.html) | Eplan Cloud user organization ID. |
| Public Property | [OrganizationName](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse~OrganizationName.html) | Organization name. (Inherited from [Eplan.IdentityClient.IdentityClientResponse](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse.html)) |
| Public Property | [OrganizationUserId](Eplan.IdentityClient.Types~Eplan.IdentityClient.AuthenticationData~OrganizationUserId.html) | Eplan Cloud user ID in the organization. |
| Public Property | [RefreshToken](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse~RefreshToken.html) | Refresh token. (Inherited from [Eplan.IdentityClient.IdentityClientResponse](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse.html)) |
| Public Property | [StatusCode](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse~StatusCode.html) | IdentityStatusCode success code. (Inherited from [Eplan.IdentityClient.IdentityClientResponse](Eplan.IdentityClient.Types~Eplan.IdentityClient.IdentityClientResponse.html)) |
| Public Property | [Sub](Eplan.IdentityClient.Types~Eplan.IdentityClient.AuthenticationData~Sub.html) | Eplan Cloud user ID in the IdentityService. |


