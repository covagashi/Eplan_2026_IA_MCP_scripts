# Verification

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification.html

---

Base class for specific test classes.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.EServices.Verification**  
      [Eplan.EplApi.EServices.FunctionVerification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.FunctionVerification.html)  
      [Eplan.EplApi.EServices.InterruptionPointVerification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.InterruptionPointVerification.html)  
      [Eplan.EplApi.EServices.PotentialVerification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PotentialVerification.html)

Syntax

**C#**



public abstract class Verification : IMessage, IVerification, IVerificationBase

public ref class Verification abstract : public IMessage, IVerification, IVerificationBase

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AdditionalObjectsFilter](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~AdditionalObjectsFilter.html) | Type of class which filters objects that are additionally passed to [IVerification.Execute](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerification~Execute.html) method. |
| Public Property | [FilterConfigPath](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~FilterConfigPath.html) |  |
| Public Property | [MessageId](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~MessageId.html) | The ID of the message. Is automatically set. |
| Public Property | [ObjectsFilter](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~ObjectsFilter.html) | Collection of objects types which will be used to determine objects passed to [IVerification.Execute](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerification~Execute.html) method. |
| Public Property | [Project](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~Project.html) | Returns project in context of which the verification is run. |
| Public Property | [Region](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~Region.html) | The region associated with the message. Is automatically set. |
| Public Property | [VerificationPermission](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~VerificationPermission.html) | The permission of a verification determines for what type of check the verification is enabled at most/ maximum. |
| Public Property | [VerificationState](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~VerificationState.html) | The VerificationState determines the actual adjusted check type whereas the permission determines what state is theoretically allowed at most. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [DoErrorMessage](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~DoErrorMessage.html) | Overloaded. Service function for the error output during a test. Text to display is taken from correct IMessage::GetMessageText method. |
| Public Method | [DoHelp](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~DoHelp.html) |  |
| Public Method | [Execute](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~Execute.html) |  |
| Public Method | [GetMessageText](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~GetMessageText.html) |  |
| Public Method | [OnEndInspection](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~OnEndInspection.html) |  |
| Public Method | [OnRegister](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~OnRegister.html) | Overloaded. If true, all messages with the same region and message id are removed after OnStartInspection is called. |
| Public Method | [OnStartInspection](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~OnStartInspection.html) |  |


