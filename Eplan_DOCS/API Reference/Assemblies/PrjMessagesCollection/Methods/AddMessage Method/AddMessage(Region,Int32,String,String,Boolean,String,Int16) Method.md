# AddMessage(Region,Int32,String,String,Boolean,String,Int16) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1297.html

---

Adds a new message associated with part number to the project's message management window. Message is related to variant = 0.

Syntax

**C#**



public ProjectMessage AddMessage( 

   IMessage.Region eRegion,

   int nErrNr,

   string strErrTextParam,

   string strPartNumber,

   string strPartVariant,

   bool bImmediateShow,

   string strAdditionalInfo

)

public:

ProjectMessage^ AddMessage( 

   IMessage.Region eRegion,

   int nErrNr,

   String^ strErrTextParam,

   String^ strPartNumber,

   String^ strPartVariant,

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
:   The message refers to this part number. Cannot be empty or null.

*strPartVariant*
:   The message refers to this part variant. Cannot be empty or null.

*bImmediateShow*
:   True\: The message is immediately displayed in the message window.

*strAdditionalInfo*
:   Additional language\-independent message text. Is saved as specified in the database. Optional parameter; this string may also be empty.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |

Remarks

Method does not check if part and part variant exist.
