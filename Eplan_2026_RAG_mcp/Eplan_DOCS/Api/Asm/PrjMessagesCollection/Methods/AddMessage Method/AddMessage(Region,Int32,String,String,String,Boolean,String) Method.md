# AddMessage(Region,Int32,String,String,String,Boolean,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1298.html

---

Adds a new message associated with part number to the project's message management window.

Syntax

**C#**



public ProjectMessage AddMessage( 

   IMessage.Region eRegion,

   int nErrNr,

   string strErrTextParam,

   string strPartNumber,

   bool bImmediateShow,

   string strAdditionalInfo

)

public:

ProjectMessage^ AddMessage( 

   IMessage.Region eRegion,

   int nErrNr,

   String^ strErrTextParam,

   String^ strPartNumber,

   bool bImmediateShow,

   String^ strAdditionalInfo

)


#### Parameters

*eRegion*
:   A message of this [IMessage.Region](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage+Region.html) is added.

*nErrNr*
:   A message with this message number is added.

*strErrTextParam*
:   reference to a parameterstring to substitute placeholders in the resource error text. Multiple parameters must be separated with "|". In the error text parameters should be signed by "%1!s!", "%2!s!" etc. If the error text doesn't have any parameter to substitute strErrTextParam must be an empty string

*strPartNumber*
:   The message refers to this part number in variant '1'. Cannot be empty or null.

*bImmediateShow*
:   True\: The message is immediately displayed in the message window.

*strAdditionalInfo*
:   Additional language\-independent message text. Is saved as specified in the database. Optional parameter; this string may also be empty.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |

Remarks

Message by default is related to variant '1' of the part. Method does not check if part exist.
