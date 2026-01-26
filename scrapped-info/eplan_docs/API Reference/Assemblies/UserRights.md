# UserRights

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights.html

---

Class for checking execute permissions.  
In the rights management module, you can assign execute permissions to individual actions. These execute permissions are also assigned to specific users. As a result, the rights management system can decide whether the logged-on user has the right to perform a specific action.  
The rights management system can be completely disabled (verification possible via [CheckUserRights](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~CheckUserRights.html) method), or it can be set to a specific operating mode (logging on with the current windows user). However, this operating mode cannot be queried or set via API.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.ApplicationFramework.UserRights**

Syntax

**C#**



public class UserRights

public ref class UserRights

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [UserRights Constructor](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~_ctor.html) |  |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddRight](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~AddRight.html) | Adds the specified right entry to the given category of the custom UserRights file. The new right name will appear in the rights management dialog. |
| Public Method | [CheckRightFor](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~CheckRightFor.html) | Checks the execute permission of an action |
| Public Method | [CheckUserRights](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~CheckUserRights.html) | Queries whether the rights management is currently active. |
| Public Method | [DeleteRight](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~DeleteRight.html) | Deletes the specified right entry from the UserRights database (rights management dialog) |
| Public Method | [GetCategories](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~GetCategories.html) | Returns the identifiers of all existing user rights categories. |
| Public Method | [GetGroups](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~GetGroups.html) | Gets the groups from user rights management, to which the specified user belongs.. |
| Public Method | [GetUser](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~GetUser.html) | Gets the user. |
| Public Method | [GetUserSID](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~GetUserSID.html) | Gets the user SID. |
| Public Method | [IsRightExisting](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~IsRightExisting.html) | Returns the right existance |
| Public Method | [SetUser](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~SetUser.html) | Sets the user. |


