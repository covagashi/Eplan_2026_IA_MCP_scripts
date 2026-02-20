# OnRegister(String,Region,Int32,Classification,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~OnRegister(String,Region,Int32,Classification,Int32).html

---

If true, all messages with the same region and message id are removed after OnStartInspection is called.

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


*iMessageId*


*eClassification*


*iOrdinal*

Remarks

Setting this property gives the effect only if it is done in method OnStartInspection.

By default this value is `false`

.
