# OnRegister Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase~OnRegister.html

---

Called by EPLAN when the new check is added to the system.

Syntax

**C#**



void OnRegister( 

   ref string strName,

   ref int iOrdinal

)

void OnRegister( 

   String^% strName,

   int% iOrdinal

)


#### Parameters

*strName*
:   The new check is saved with this name in the system.

*iOrdinal*
:   Overload level for the new check.

Remarks

It is not allowed to override the functionality of an existing check. Only the message text can be changed as described in [IMessage.OnRegister](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage~OnRegister.html) It is not possible to overwrite an existing verification. The overload level is just needed for registration purposes.
