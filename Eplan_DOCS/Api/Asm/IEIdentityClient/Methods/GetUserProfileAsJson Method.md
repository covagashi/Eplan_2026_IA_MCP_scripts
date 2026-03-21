# GetUserProfileAsJson Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~GetUserProfileAsJson.html

---

Gets Eplan cloud user profile information in a JSON format.

Syntax

**C#**



Task<string> GetUserProfileAsJson()

Task<String^>^ GetUserProfileAsJson();


#### Return Value

user profile information in a JSON format.

Remarks

The returned JSON string contains information such as DisplayName, OrganizationName, Email etc.
