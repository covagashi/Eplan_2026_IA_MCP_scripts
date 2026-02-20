# DeleteRight Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~DeleteRight.html

---

Deletes the specified right entry from the UserRights database (rights management dialog)

Syntax

**C#**



public bool DeleteRight( 

   string strRightname

)

public:

bool DeleteRight( 

   String^ strRightname

)


#### Parameters

*strRightname*
:   name of the user right entry to remove

#### Return Value

TRUE in case the right was successfully removed from the rights management database.

Remarks

The currently logged-in user must have the URShowAdministrationDialog right, this is the right to work on user rights. Any group assignments of this right are removed.
