# PartVerification

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification.html

---

Base class for specific test classes.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.EServices.PartVerification**

Syntax

**C#**



public abstract class PartVerification : IMessage, IPartVerification, IVerificationBase

public ref class PartVerification abstract : public IMessage, IPartVerification, IVerificationBase

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [FilterConfigPath](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification~FilterConfigPath.html) |  |
| Public Property | [MessageId](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification~MessageId.html) | The ID of the message. |
| Public Property | [Region](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification~Region.html) | The region associated with the message. |
| Public Property | [VerificationPermission](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification~VerificationPermission.html) |  |
| Public Property | [VerificationState](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification~VerificationState.html) | The VerificationState determines the actual adjusted check type whereas the permission determines what state is theoretically allowed at most. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [DoErrorMessage](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification~DoErrorMessage.html) | Overloaded. Service function for the error output during a test. Text to display is taken from correct IMessage::GetMessageText method. |
| Public Method | [DoHelp](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification~DoHelp.html) |  |
| Public Method | [Execute](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification~Execute.html) |  |
| Public Method | [GetMessageText](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification~GetMessageText.html) |  |
| Public Method | [OnEndInspection](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification~OnEndInspection.html) |  |
| Public Method | [OnRegister](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification~OnRegister.html) | Overloaded. Called by Eplan when the new project message is added to the system. If a new project message was added to a registered add-in, the add-in must be registered over again. |
| Public Method | [OnStartInspection](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification~OnStartInspection.html) |  |


