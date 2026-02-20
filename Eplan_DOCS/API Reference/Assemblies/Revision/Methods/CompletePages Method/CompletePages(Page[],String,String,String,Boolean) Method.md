# CompletePages(Page[],String,String,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~CompletePages(Page[],String,String,String,Boolean).html

---

Completes modification of selected pages in the current revision of a project and can update the evaluations in the selection. Used for change tracking.

Syntax

**C#**



public void CompletePages( 

   Page[] pagesToComplete,

   string strIndex,

   string strRevDescription,

   string strReasonOfChange,

   bool bEvaluate

)

public:

void CompletePages( 

   array<Page^>^ pagesToComplete,

   String^ strIndex,

   String^ strRevDescription,

   String^ strReasonOfChange,

   bool bEvaluate

)


#### Parameters

*pagesToComplete*
:   An array of pages to complete.

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

Used for change tracking. When a logging revision starts, every changed page gets the marker "Draft" on it. With this function a page is completed, a page revision is created (visible in the page revision properties) and the draft is removed. When the revision belongs to an active project section, only the pages of this section are completed.
