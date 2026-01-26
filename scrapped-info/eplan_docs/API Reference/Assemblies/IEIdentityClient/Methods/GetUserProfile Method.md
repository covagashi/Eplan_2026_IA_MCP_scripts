# GetUserProfile Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~GetUserProfile.html

---

Gets Eplan cloud user profile information.

Syntax

**C#**



Task<IdentityClientResponse> GetUserProfile()

Task<IdentityClientResponse^>^ GetUserProfile();


#### Return Value

IdentityClientResponse: operation result.

Remarks

The returned CloudUserProfile object contains information such as DisplayName, OrganizationName, Email etc.
