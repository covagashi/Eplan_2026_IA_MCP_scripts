# AddMessage Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseMessages~AddMessage.html

---

Adds a new message associated with part number to the PartsDatabase message management window.

Syntax

**C#**



public MDPartsMessage AddMessage( 

   int nErrNr,

   string strErrTextParam,

   string strPartNumber,

   string strPartVariant

)

public:

MDPartsMessage^ AddMessage( 

   int nErrNr,

   String^ strErrTextParam,

   String^ strPartNumber,

   String^ strPartVariant

)


#### Parameters

*nErrNr*
:   A message with this message number is added.

*strErrTextParam*
:   It references to a parameter string to substitute placeholders in the resource error text. Multiple parameters must be separated with "|". In the error text parameters should be signed by "%1!s!", "%2!s!" etc. If the error text doesn't have any parameter to substitute strErrTextParam must be an empty string

*strPartNumber*
:   The message refers to this part number. Cannot be empty or null.

*strPartVariant*
:   The message refers to this part variant. Cannot be empty or null.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |

Remarks

Method does not check if part and part variant exist.
