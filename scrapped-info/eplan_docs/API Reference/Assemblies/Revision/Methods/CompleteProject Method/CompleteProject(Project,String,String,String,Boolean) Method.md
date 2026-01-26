# CompleteProject(Project,String,String,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~CompleteProject(Project,String,String,String,Boolean).html

---

Completes current revision of a project and can evaluate the project. Used for change tracking.

Syntax

**C#**



public void CompleteProject( 

   Project oProjectToComplete,

   string strIndex,

   string strRevDescription,

   string strReasonOfChange,

   bool bEvaluate

)

public:

void CompleteProject( 

   Project^ oProjectToComplete,

   String^ strIndex,

   String^ strRevDescription,

   String^ strReasonOfChange,

   bool bEvaluate

)


#### Parameters

*oProjectToComplete*
:   A project to complete.

*strIndex*
:   Name of the new revision.

*strRevDescription*
:   Description of the new revision.

*strReasonOfChange*
:   Additional description of the new revision.

*bEvaluate*
:   If set to true, the evaluation is done before completing.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the action. |

Remarks

Used for change tracking. All pages not completed so far are completed now. When a revision for a project section is active, only the pages and installation spaces of this project section are protected. The project itself stays writable. Otherwise the project is converted to a read-only revision project.
