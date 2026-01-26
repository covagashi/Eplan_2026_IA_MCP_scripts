# CheckRightFor Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~CheckRightFor.html

---

Checks the execute permission of an action

Syntax

**C#**



public bool CheckRightFor( 

   string strRight

)

public:

bool CheckRightFor( 

   String^ strRight

)


#### Parameters

*strRight*
:   Name of the execute permission to be checked.

#### Return Value

'¢ TRUE: Action is granted execute permission.  
'¢ FALSE: The action must not be executed by the current user.

Remarks

Before executing newly programmed functions, the API programmer should check a right that is relatively similar to that of the new function. If, for example, a function is implemented that generates new pages, the right to create pages (XGedNewSchemePage) should be queried beforehand. If you check for a right, which is not yet added to the UserRights database, this right is always granted.

Example

Example of querying a right

**C#**

```
UserRights oUserRights = new UserRights();

bool bRights = oUserRights.CheckUserRights(); // is the user rights management activated?

if (bRights)

{

  bool bAnRight= oUserRights.CheckRightFor("XPLEditorStart");

}
```
