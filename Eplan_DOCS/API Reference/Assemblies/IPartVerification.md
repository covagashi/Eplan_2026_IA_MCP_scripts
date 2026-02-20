# IPartVerification

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IPartVerification.html

---

Interface declaration for a part check in EPLAN. If an add-in wants to add an undefined part check to EPLAN projects this interface must be implemented by a class of the add-in.

Syntax

**C#**



public interface IPartVerification : IMessage, IVerificationBase

public interface class IPartVerification : public IMessage, IVerificationBase

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [DoHelp](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage~DoHelp.html) | Called by EPLAN when the help text to the message should be shown. the function itself must take care to call the matching help system with the correct language. The easiest way is to call a simple dialog or message box. (Inherited from [Eplan.EplApi.EServices.IMessage](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage.html)) |
| Method | [Execute](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IPartVerification~Execute.html) | Called by EPLAN when a specific MDPartsDatabaseItem is to be checked. Currently only MDPart objects are passed to this method. Implements the "check." |
| Method | [GetMessageText](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage~GetMessageText.html) | Called by EPLAN when the message text should be shown. (Inherited from [Eplan.EplApi.EServices.IMessage](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage.html)) |
| Method | [OnEndInspection](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase~OnEndInspection.html) | Called by EPLAN when a check routine has been completed. (Inherited from [Eplan.EplApi.EServices.IVerificationBase](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase.html)) |
| Method | [OnRegister](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase~OnRegister.html) | Called by EPLAN when the new check is added to the system. (Inherited from [Eplan.EplApi.EServices.IVerificationBase](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase.html)) |
| Method | [OnStartInspection](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase~OnStartInspection.html) | Called by EPLAN when a check routine starts in the system. (Inherited from [Eplan.EplApi.EServices.IVerificationBase](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase.html)) |


