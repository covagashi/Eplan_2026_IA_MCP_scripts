# DoErrorMessage(StorableObject,StorableObject,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~DoErrorMessage(StorableObject,StorableObject,String).html

---

Service function for the error output during a test. Text to display is taken from correct IMessage::GetMessageText method.

Syntax

**C#**



public virtual void DoErrorMessage( 

   StorableObject oFirstObject,

   StorableObject oSecondObject,

   string strTextParameter

)

public:

virtual void DoErrorMessage( 

   StorableObject^ oFirstObject,

   StorableObject^ oSecondObject,

   String^ strTextParameter

)


#### Parameters

*oFirstObject*
:   The error refers to this object.

*oSecondObject*
:   Another object that caused the error.

*strTextParameter*
:   Parameter values for the message text. This value is used only with messages that use %1!s! variable in their definition.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when `oFirstObject` is invalid or NULL. |
