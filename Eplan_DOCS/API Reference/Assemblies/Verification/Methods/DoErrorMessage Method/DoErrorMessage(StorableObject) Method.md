# DoErrorMessage(StorableObject) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~DoErrorMessage(StorableObject).html

---

Service function for the error output during a test. Text to display is taken from correct IMessage::GetMessageText method.

Syntax

**C#**



public virtual void DoErrorMessage( 

   StorableObject oObject

)

public:

virtual void DoErrorMessage( 

   StorableObject^ oObject

)


#### Parameters

*oObject*
:   The error refers to this object.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when `oObject` is invalid or NULL. |
