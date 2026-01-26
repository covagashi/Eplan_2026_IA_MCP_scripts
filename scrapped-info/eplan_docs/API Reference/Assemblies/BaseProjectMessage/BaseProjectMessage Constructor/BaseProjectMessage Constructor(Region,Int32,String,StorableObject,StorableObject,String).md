# BaseProjectMessage Constructor(Region,Int32,String,StorableObject,StorableObject,String)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1295.html

---

Adds a new message associated with part number to the project's message management window.

Syntax

**C#**



public ProjectMessage AddMessage( 

   IMessage.Region eRegion,

   int nErrNr,

   string strErrTextParam,

   string strPartNumber,

   string strPartVariant,

   bool bImmediateShow,

   string strAdditionalInfo,

   short nCreationType

)

public:

ProjectMessage^ AddMessage( 

   IMessage.Region eRegion,

   int nErrNr,

   String^ strErrTextParam,

   String^ strPartNumber,

   String^ strPartVariant,

   bool bImmediateShow,

   String^ strAdditionalInfo,

   short nCreationType

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

*nCreationType*
:   Additional information about the source of the message. Possible values are: 0 - undefined, 1 - Online verification 2 - Offline verification 3 - Explicit creation Note: In order to add a message with nCreationType = 3, it must be registered and enabled in the message management.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |

Remarks

Method does not check if part and part variant exist.
