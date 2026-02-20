# OnStartInspection Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase~OnStartInspection.html

---

Called by EPLAN when a check routine starts in the system.

Syntax

**C#**



void OnStartInspection( 

   bool bOnline

)

void OnStartInspection( 

   bool bOnline

)


#### Parameters

*bOnline*
:   True: An online check is made. False: An offline check is made.

Remarks

Note: OnStartInspection/OnEndInspection methods are called for each verification registered in the system when the check routine starts/ends regardless of type of the check (online/offline) and regardless of the verification's category filter.
