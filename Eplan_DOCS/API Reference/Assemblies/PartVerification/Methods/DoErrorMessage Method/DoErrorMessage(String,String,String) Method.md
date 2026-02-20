# DoErrorMessage(String,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification~DoErrorMessage(String,String,String).html

---

Service function for the error output during a test. Text to display is taken from correct IMessage::GetMessageText method.

Syntax

**C#**



public virtual void DoErrorMessage( 

   string strPartNumber,

   string strPartVariant,

   string strTextParameter

)

public:

virtual void DoErrorMessage( 

   String^ strPartNumber,

   String^ strPartVariant,

   String^ strTextParameter

)


#### Parameters

*strPartNumber*
:   The error refers to part with this part number. Cannot be empty or null.

*strPartVariant*
:   The error refers to part in this part variant. Cannot be empty or null.

*strTextParameter*
:   Parameter values for the message text. This value is used only with messages that use %1!s! variable in their definition.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when `strPartNumber` or `strPartVariant` is empty or NULL. |

Remarks

Method does not check if part and part variant exist.
