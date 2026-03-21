# DoErrorMessage(StorableObject,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~DoErrorMessage(StorableObject,String).html

---

Service function for the error output during a test. Text to display is taken from correct IMessage::GetMessageText method.

Syntax

**C#**



public virtual void DoErrorMessage( 

   StorableObject oObject,

   string strTextParameter

)

public:

virtual void DoErrorMessage( 

   StorableObject^ oObject,

   String^ strTextParameter

)


#### Parameters

*oObject*
:   The error refers to this object.

*strTextParameter*
:   Parameter values for the message text. This value is used only with messages that use %1!s! variable in their definition.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when `oObject` is invalid or NULL. |
