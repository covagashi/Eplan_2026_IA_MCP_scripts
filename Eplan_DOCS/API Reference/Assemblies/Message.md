# Message

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Message.html

---

Base class for electrotechnical messages. If an add-in wants to add an undefined project message to EPLAN projects, then the class of the add-in must inherit from the Eplan.EplApi.EServices.Message class.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.EServices.Message**

Syntax

**C#**



public abstract class Message : IMessage

public ref class Message abstract : public IMessage

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [MessageState](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Message~MessageState.html) | The MessageState determines the actual adjusted check type |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [DoHelp](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Message~DoHelp.html) | Called by EPLAN when the help text to the message should be shown. the function itself must take care to call the matching help system with the correct language. The easiest way is to call a simple dialog or message box. |
| Public Method | [GetMessageText](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Message~GetMessageText.html) | Called by EPLAN when the message text should be shown. |
| Public Method | [OnRegister](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Message~OnRegister.html) | Called by EPLAN when the new project message is added to the system. If a new project message was added to a registered add-in, the add-in must be registered over again. |


