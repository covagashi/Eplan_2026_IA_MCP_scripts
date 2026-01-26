# IsPartsSelectionOnProject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PartsService~IsPartsSelectionOnProject.html

---

Check if the project's parts selection is set to project.

Syntax

**C#**



public bool IsPartsSelectionOnProject( 

   Project oProject,

   ref string strInfoForUser

)

public:

bool IsPartsSelectionOnProject( 

   Project^ oProject,

   String^% strInfoForUser

)


#### Parameters

*oProject*
:   The project to check

*strInfoForUser*
:   [out] The info for a user where to change this setting

#### Return Value

true is the parts selection is set to project and not to user defined.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments |

Remarks

This is configured in Settings: Part selection dialog. Either the parts selection is set to Project or user defined.
