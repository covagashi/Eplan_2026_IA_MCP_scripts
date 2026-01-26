# InitIdentityClient Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.IdentityClient.Authentification~Eplan.IdentityClient.Authentification.IEIdentityClient~InitIdentityClient.html

---

Initializes Eplan IdentityClient

Syntax

**C#**



IdentityClientResponse InitIdentityClient( 

   string strMainClientId,

   ApplicationMode mode,

   string strLocale,

   string strScopes

)

IdentityClientResponse^ InitIdentityClient( 

   String^ strMainClientId,

   ApplicationMode mode,

   String^ strLocale,

   String^ strScopes

)


#### Parameters

*strMainClientId*
:   Application main ClientId name. E.g. DesktopPlatformWithConsents, HarnessProD

*mode*
:   Interactive (with UI) or Batch application mode.

*strLocale*
:   Language, e.g. "en-US" or "de-DE".

*strScopes*
:   For internal use (parameter is set automatically).

#### Return Value

IdentityClientResponse: operation result.

Remarks

IdentityClient should be initialized by calling this method. This is necessary in order to be able to use this interface.
