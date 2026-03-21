# CreateComparisonProject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~CreateComparisonProject.html

---

Creates a comparison project for the specified project. Used for property comparison.

Syntax

**C#**



public void CreateComparisonProject( 

   Project oProject,

   string strRevisionName,

   string strComment,

   bool bTemporary

)

public:

void CreateComparisonProject( 

   Project^ oProject,

   String^ strRevisionName,

   String^ strComment,

   bool bTemporary

)


#### Parameters

*oProject*
:   The project which will be copied as comparison project.

*strRevisionName*
:   Revision name. Full link file name of the copied project.

*strComment*
:   Comment on the created comparison project.

*bTemporary*
:   If set to true, the comparison project is marked as temporary (not read-only).

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created or an error occurred when creating the comparison project. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred when creating the comparison project. |

Remarks

Used for property comparison.
