# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase_methods.html

---

For a list of all members of this type, see [IVerificationBase members](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [DoHelp](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage~DoHelp.html) | Called by EPLAN when the help text to the message should be shown. the function itself must take care to call the matching help system with the correct language. The easiest way is to call a simple dialog or message box. (Inherited from [Eplan.EplApi.EServices.IMessage](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage.html)) |
| Method | [GetMessageText](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage~GetMessageText.html) | Called by EPLAN when the message text should be shown. (Inherited from [Eplan.EplApi.EServices.IMessage](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage.html)) |
| Method | [OnEndInspection](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase~OnEndInspection.html) | Called by EPLAN when a check routine has been completed. |
| Method | [OnRegister](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase~OnRegister.html) | Called by EPLAN when the new check is added to the system. |
| Method | [OnStartInspection](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase~OnStartInspection.html) | Called by EPLAN when a check routine starts in the system. |


