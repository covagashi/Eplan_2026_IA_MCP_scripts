# IMessage

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage.html

---

Interface declaration for an electrotechnical message in EPLAN. If an add-in wants to add an undefined project message to EPLAN projects, then the class of the add-in must inherit from the Eplan.EplApi.EServices.Message class.

Syntax

**C#**



public interface IMessage

public interface class IMessage

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [DoHelp](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage~DoHelp.html) | Called by EPLAN when the help text to the message should be shown. the function itself must take care to call the matching help system with the correct language. The easiest way is to call a simple dialog or message box. |
| Method | [GetMessageText](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage~GetMessageText.html) | Called by EPLAN when the message text should be shown. |
| Method | [OnRegister](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage~OnRegister.html) | Called by EPLAN when the new project message is added to the system. If a new project message was added to a registered add-in, the add-in must be registered over again. |


