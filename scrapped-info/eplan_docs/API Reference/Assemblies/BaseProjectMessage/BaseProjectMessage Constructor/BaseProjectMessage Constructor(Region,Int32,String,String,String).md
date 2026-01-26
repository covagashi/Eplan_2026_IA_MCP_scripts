# BaseProjectMessage Constructor(Region,Int32,String,String,String)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.BaseProjectMessage~_ctor(Region,Int32,String,String,String).html

---

constructor

Syntax

**C#**



public BaseProjectMessage( 

   IMessage.Region eRegion,

   int nErrNr,

   string strErrTextParam,

   string strPartNumber,

   string strAdditionalInf

)

public:

BaseProjectMessage( 

   IMessage.Region eRegion,

   int nErrNr,

   String^ strErrTextParam,

   String^ strPartNumber,

   String^ strAdditionalInf

)


#### Parameters

*eRegion*
:   [IMessage.Region](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage+Region.html) of this message.

*nErrNr*
:   Message number.

*strErrTextParam*
:   The replacement text for this message. This string may also be empty.

*strPartNumber*
:   The message refers to variant '1' of this part number. Cannot be empty or null.

*strAdditionalInf*
:   Additional language-independent message text. Is saved as specified in the database. This string may also be empty.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when strPartNumber is empty or null. |
