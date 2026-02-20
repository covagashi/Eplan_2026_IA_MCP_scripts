# OnRegister(String,Region,Int32,Classification,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification~OnRegister(String,Region,Int32,Classification,Int32).html

---

Called by Eplan when the new project message is added to the system. If a new project message was added to a registered add-in, the add-in must be registered over again.

Syntax

**C#**



public abstract void OnRegister( 

   ref string strCreator,

   ref IMessage.Region eRegion,

   ref int iMessageId,

   ref IMessage.Classification eClassification,

   ref int iOrdinal

)

public:

abstract void OnRegister( 

   String^% strCreator,

   IMessage.Region% eRegion,

   int% iMessageId,

   IMessage.Classification% eClassification,

   int% iOrdinal

)


#### Parameters

*strCreator*


*eRegion*
:   The new project message will be added to this [IMessage.Region](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage+Region.html). Part verifications can be registered only in PartMasterData region.

*iMessageId*
:   serial number inside the chosen region

*eClassification*
:   Default [IMessage.Classification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage+Classification.html) of the new message. The [IMessage.Classification](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage+Classification.html) could be changed in the project setting dialog at run time.

*iOrdinal*
:   The new message could overwrite an existing message which has the same [IMessage.Region](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage+Region.html) and the same iMessageId, if the ordinal number of the new message is higher. (default\: 20)

Remarks

PartVerifications can be registered only in PartMasterData region. By overriding an existing message, it is only possible to change the message text, but not the classification etc.
