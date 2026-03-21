# IPotentialVerification

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IPotentialVerification.html

---

Interface for a special verification class.

Syntax

**C#**



public interface IPotentialVerification : IMessage, IVerification, IVerificationBase

public interface class IPotentialVerification : public IMessage, IVerification, IVerificationBase

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [DoHelp](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage~DoHelp.html) | Called by EPLAN when the help text to the message should be shown. the function itself must take care to call the matching help system with the correct language. The easiest way is to call a simple dialog or message box. (Inherited from [Eplan.EplApi.EServices.IMessage](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage.html)) |
| Method | [Execute](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerification~Execute.html) | Called by EPLAN when a specific object is to be checked. Implements the "check." (Inherited from [Eplan.EplApi.EServices.IVerification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerification.html)) |
| Method | [GetMessageText](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage~GetMessageText.html) | Called by EPLAN when the message text should be shown. (Inherited from [Eplan.EplApi.EServices.IMessage](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage.html)) |
| Method | [OnEndInspection](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase~OnEndInspection.html) | Called by EPLAN when a check routine has been completed. (Inherited from [Eplan.EplApi.EServices.IVerificationBase](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase.html)) |
| Method | [OnRegister](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase~OnRegister.html) | Called by EPLAN when the new check is added to the system. (Inherited from [Eplan.EplApi.EServices.IVerificationBase](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase.html)) |
| Method | [OnStartInspection](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase~OnStartInspection.html) | Called by EPLAN when a check routine starts in the system. (Inherited from [Eplan.EplApi.EServices.IVerificationBase](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase.html)) |


