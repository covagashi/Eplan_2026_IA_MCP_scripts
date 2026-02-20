# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage_methods.html

---

For a list of all members of this type, see [IMessage members](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [DoHelp](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage~DoHelp.html) | Called by EPLAN when the help text to the message should be shown. the function itself must take care to call the matching help system with the correct language. The easiest way is to call a simple dialog or message box. |
| Method | [GetMessageText](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage~GetMessageText.html) | Called by EPLAN when the message text should be shown. |
| Method | [OnRegister](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage~OnRegister.html) | Called by EPLAN when the new project message is added to the system. If a new project message was added to a registered add-in, the add-in must be registered over again. |


