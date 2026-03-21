# PotentialVerification

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PotentialVerification.html

---

Base class for specific verification classes that only check potentials.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.EServices.Verification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification.html)  
      **Eplan.EplApi.EServices.PotentialVerification**

Syntax

**C#**



public abstract class PotentialVerification : Verification, IMessage, IPotentialVerification, IVerification, IVerificationBase

public ref class PotentialVerification abstract : public Verification, IMessage, IPotentialVerification, IVerification, IVerificationBase


Remarks

\ \ When using following inheritance hierarchy : Interface, inheriting abstract class, and then normal class, (like IMessage-\>PotentialVerification -\>VerificationExample) under .Net 2.0 there is a run-time error while loading add-in ("Unable to load one or more of the requested types. Retrieve the LoaderExceptions property for more information")

Example

Current workaround is to add interface names after class identifier, so such declaration as:

**C#**

```
publicclass VerificationExample: PotentialVerification

{}

//Should be substituted by :

publicclass VerificationExample: PotentialVerification : IVerification : IMessage

{}
```

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AdditionalObjectsFilter](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PotentialVerification~AdditionalObjectsFilter.html) | Overridden. Type of class which filters objects that are additionally passed to [IVerification.Execute](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerification~Execute.html) method. |
| Public Property | [FilterConfigPath](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PotentialVerification~FilterConfigPath.html) | Overridden. |
| Public Property | [MessageId](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~MessageId.html) | The ID of the message. Is automatically set. (Inherited from [Eplan.EplApi.EServices.Verification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification.html)) |
| Public Property | [ObjectsFilter](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PotentialVerification~ObjectsFilter.html) | Overridden. Collection of objects types which will be used to determine objects passed to [IVerification.Execute](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerification~Execute.html) method. |
| Public Property | [Project](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~Project.html) | Returns project in context of which the verification is run. (Inherited from [Eplan.EplApi.EServices.Verification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification.html)) |
| Public Property | [Region](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~Region.html) | The region associated with the message. Is automatically set. (Inherited from [Eplan.EplApi.EServices.Verification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification.html)) |
| Public Property | [VerificationPermission](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~VerificationPermission.html) | The permission of a verification determines for what type of check the verification is enabled at most/ maximum. (Inherited from [Eplan.EplApi.EServices.Verification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification.html)) |
| Public Property | [VerificationState](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~VerificationState.html) | The VerificationState determines the actual adjusted check type whereas the permission determines what state is theoretically allowed at most. (Inherited from [Eplan.EplApi.EServices.Verification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [DoErrorMessage](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~DoErrorMessage.html) | Overloaded. Service function for the error output during a test. Text to display is taken from correct IMessage::GetMessageText method. (Inherited from [Eplan.EplApi.EServices.Verification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification.html)) |
| Public Method | [DoHelp](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~DoHelp.html) | (Inherited from [Eplan.EplApi.EServices.Verification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification.html)) |
| Public Method | [Execute](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~Execute.html) | (Inherited from [Eplan.EplApi.EServices.Verification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification.html)) |
| Public Method | [GetAllPotentialsWithSameName](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PotentialVerification~GetAllPotentialsWithSameName.html) | Returns all potentials of the project with the same name. Can be called within the Execute function. |
| Public Method | [GetMessageText](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~GetMessageText.html) | (Inherited from [Eplan.EplApi.EServices.Verification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification.html)) |
| Public Method | [OnEndInspection](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~OnEndInspection.html) | (Inherited from [Eplan.EplApi.EServices.Verification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification.html)) |
| Public Method | [OnRegister](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~OnRegister.html) | Overloaded. If true, all messages with the same region and message id are removed after OnStartInspection is called. (Inherited from [Eplan.EplApi.EServices.Verification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification.html)) |
| Public Method | [OnStartInspection](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~OnStartInspection.html) | (Inherited from [Eplan.EplApi.EServices.Verification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification.html)) |


