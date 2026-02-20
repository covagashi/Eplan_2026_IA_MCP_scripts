# CheckUserRights Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~CheckUserRights.html

---

Queries whether the rights management is currently active.

Syntax

**C#**



public bool CheckUserRights()

public:

bool CheckUserRights();


#### Return Value

'¢ TRUE: Rights management activated in the system  
'¢ FALSE: No rights management activated in the system

Remarks

This method does not change the current mode of rights management. It only checks, whether the rights management is active or not.
