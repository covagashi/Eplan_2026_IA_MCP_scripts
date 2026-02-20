# SetProductInfo Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~SetProductInfo.html

---

Sets product information

Syntax

**C#**



bool SetProductInfo( 

   ProductInfo productInfo,

   Dictionary<string,string> additionalProductInfo

)

bool SetProductInfo( 

   ProductInfo^ productInfo,

   Dictionary<String^,String^>^ additionalProductInfo

)


#### Parameters

*productInfo*
:   Product Information

*additionalProductInfo*
:   Additional Product Information

#### Return Value

true if product information could be sent to the IdentityClient. Otherwise false.
