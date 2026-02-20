# IsPartsSelectionOnPartsDatabase Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PartsService~IsPartsSelectionOnPartsDatabase.html

---

Check if the user parts selection is set to parts database.

Syntax

**C#**



public bool IsPartsSelectionOnPartsDatabase( 

   Project oProject,

   ref string strInfoForUser

)

public:

bool IsPartsSelectionOnPartsDatabase( 

   Project^ oProject,

   String^% strInfoForUser

)


#### Parameters

*oProject*
:   The project to check

*strInfoForUser*
:   [out] The info for a user where to change this setting

#### Return Value

true is the project's parts selection is set to user defined and the user parts selection is set to parts database.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments |

Remarks

This is configured in Settings: Project + Part selection dialog. Either the parts selection is set to Project or user defined. The additional setting is configured in User + Part selection dialog.
