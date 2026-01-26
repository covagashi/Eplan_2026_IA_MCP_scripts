# GetGroups Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~GetGroups.html

---

Gets the groups from user rights management, to which the specified user belongs..

Syntax

**C#**



public StringCollection GetGroups( 

   string strUserSID

)

public:

StringCollection^ GetGroups( 

   String^ strUserSID

)


#### Parameters

*strUserSID*
:   SID of user.

#### Return Value

The groups, the user belongs to.
