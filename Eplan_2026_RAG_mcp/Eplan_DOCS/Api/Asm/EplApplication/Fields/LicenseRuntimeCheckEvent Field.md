# LicenseRuntimeCheckEvent Field

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication~LicenseRuntimeCheckEvent.html

---

License runtime check callback event

Syntax

**C#**



public static EplApplication.LicenseRuntimeCheckCallbackHandler LicenseRuntimeCheckEvent

public:

static EplApplication.LicenseRuntimeCheckCallbackHandler^ LicenseRuntimeCheckEvent


Example

**C#**

```
Dispatcher m_Dispatcher = Dispatcher.CurrentDispatcher;       

EplApplication.LicenseRuntimeCheckCommands LicenseCallbackHandler(int nError, String strError, EplApplication.LicenseRuntimeCheckModes nLicenseRuntimeCheckMode)

{

   //we should be in the UI Thread.

   EplApplication.LicenseRuntimeCheckCommands response = EplApplication.LicenseRuntimeCheckCommands.Cancel;

   if (nLicenseRuntimeCheckMode == EplApplication.LicenseRuntimeCheckModes.TryCancel)

   {

       if (new Decider().Decide(EnumDecisionType.eYesNoDecision, "License error - Retry","",  EnumDecisionReturn.eYES, EnumDecisionReturn.eNO) == EnumDecisionReturn.eYES)

           response = EplApplication.LicenseRuntimeCheckCommands.Retry;

       else

           response = EplApplication.LicenseRuntimeCheckCommands.Cancel;

   }

   else if (nLicenseRuntimeCheckMode == EplApplication.LicenseRuntimeCheckModes.Cancel)

   {

       new Decider().Decide(EnumDecisionType.eOkDecision, strError, "License error - Cancel", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

       response = EplApplication.LicenseRuntimeCheckCommands.Cancel;

   }

   return response;

}

delegate EplApplication.LicenseRuntimeCheckCommands LicenseCallbackHandlerDel(int nError, String strError, EplApplication.LicenseRuntimeCheckModes nLicenseRuntimeCheckMode);

EplApplication.LicenseRuntimeCheckCommands MyLicenseCallbackHandler(int nError, String strError, EplApplication.LicenseRuntimeCheckModes nLicenseRuntimeCheckMode)

{

   EplApplication.LicenseRuntimeCheckCommands response = EplApplication.LicenseRuntimeCheckCommands.Cancel;

   if (m_Dispatcher.CheckAccess())

   {

       //we are in the UI thread

       response = LicenseCallbackHandler(nError, strError, nLicenseRuntimeCheckMode);

   }

   else

   {

       //we are not in the UI thread, so we should switch to UI thread in order to use the UI control

       var obj = 

           m_Dispatcher.Invoke

               (                           

                   new LicenseCallbackHandlerDel(LicenseCallbackHandler),

                   new Object[] { nError, strError, nLicenseRuntimeCheckMode }

                   );

       response = (EplApplication.LicenseRuntimeCheckCommands)obj;

   }

   return response;

}
```

Remarks

Event triggered if a connection to the license system is broken (no connection to a license server nor a dongle). License runtime check Callback Handler should be registered by this event.
