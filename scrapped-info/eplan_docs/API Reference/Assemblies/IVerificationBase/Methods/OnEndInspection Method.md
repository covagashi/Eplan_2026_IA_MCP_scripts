# OnEndInspection Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase~OnEndInspection.html

---

Called by EPLAN when a check routine has been completed.

Syntax

**C#**



void OnEndInspection()

void OnEndInspection();


Remarks

Note: OnStartInspection/OnEndInspection methods are called for each verification registered in the system when the check routine starts/ends regardless of type of the check (online/offline) and regardless of the verification's category filter.
