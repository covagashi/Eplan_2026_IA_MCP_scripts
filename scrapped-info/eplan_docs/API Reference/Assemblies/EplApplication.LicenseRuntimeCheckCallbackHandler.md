# EplApplication.LicenseRuntimeCheckCallbackHandler

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication+LicenseRuntimeCheckCallbackHandler.html

---

License runtime check Callback handler delegate.

Syntax

**C#**



public delegate EplApplication.LicenseRuntimeCheckCommands EplApplication.LicenseRuntimeCheckCallbackHandler( 

   int nError,

   string strError,

   EplApplication.LicenseRuntimeCheckModes nLicenseRuntimeCheckMode

)

public delegate EplApplication.LicenseRuntimeCheckCommands EplApplication.LicenseRuntimeCheckCallbackHandler( 

   int nError,

   String^ strError,

   EplApplication.LicenseRuntimeCheckModes nLicenseRuntimeCheckMode

)


#### Parameters

*nError*
:   Error number.

*strError*
:   Error message.

*nLicenseRuntimeCheckMode*
:   License runtime check mode. [EplApplication](Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication.html)

Remarks

When client application implements this handler and register it by LicenseRuntimeCheckEvent, it will be called if a connection with a license system is broken (no connection to a license server nor a dongle).
