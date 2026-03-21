# CreateTransient(Project,SymbolReference,SymbolReference) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1294.html

---

constructor

Syntax

**C#**



public BaseProjectMessage( 

   IMessage.Region eRegion,

   int nErrNr,

   string strErrTextParam,

   StorableObject oObject1,

   StorableObject oObject2,

   string strAdditionalInf

)

public:

BaseProjectMessage( 

   IMessage.Region eRegion,

   int nErrNr,

   String^ strErrTextParam,

   StorableObject^ oObject1,

   StorableObject^ oObject2,

   String^ strAdditionalInf

)


#### Parameters

*eRegion*
:   [IMessage.Region](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage+Region.html) of this message.

*nErrNr*
:   Message number.

*strErrTextParam*
:   The replacement text for this message. This string may also be empty.

*oObject1*
:   The message refers to this object. Can also be NULL.

*oObject2*
:   A second object to which this message also refers. Can also be NULL.

*strAdditionalInf*
:   Additional language-independent message text. Is saved as specified in the database. This string may also be empty.
