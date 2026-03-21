# AddRight Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.UserRights~AddRight.html

---

Adds the specified right entry to the given category of the custom UserRights file. The new right name will appear in the rights management dialog.

Syntax

**C#**



public bool AddRight( 

   string strRightname,

   string strCategory

)

public:

bool AddRight( 

   String^ strRightname,

   String^ strCategory

)


#### Parameters

*strRightname*
:   right name string

*strCategory*
:   category name string. Only existing categories can be used. You can get the existing categories by the GetCategories method. You need to set the complete category name, you find in the StringCollection returned by GetCategory.

#### Return Value

TRUE in case the new right was successfully added to the rights management database.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ApplicationException](#) | Thrown when logged-in user has not enough right to work on user rights. |
| [System.ArgumentException](#) | Thrown when given right `strRightname` already exist. |
| [System.ArgumentException](#) | Thrown when category `strCategory` does not exist. |

Remarks

The currently logged-in user must have the URShowAdministrationDialog right, this is the right to work on user rights. The custom user rights will be saved to the file "$(EPLAN\_DATA)\\Administration\\customrights.erm". The system administrator needs to protect this file from changes by unauthorized persons.
