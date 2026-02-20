# CompareProjects(Project,Project,Boolean,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~CompareProjects(Project,Project,Boolean,String,Boolean).html

---

Compares all possible properties of a project to a comparison project. Used for property comparison.

Syntax

**C#**



public void CompareProjects( 

   Project oProject,

   Project oRevision,

   bool bRemoveOldMarkers,

   string strRevisionMarker,

   bool bAppendResult

)

public:

void CompareProjects( 

   Project^ oProject,

   Project^ oRevision,

   bool bRemoveOldMarkers,

   String^ strRevisionMarker,

   bool bAppendResult

)


#### Parameters

*oProject*
:   Project to compare.

*oRevision*
:   Comparison project to compare to.

*bRemoveOldMarkers*
:   If set to true, old revision markers will be deleted before comparing.

*strRevisionMarker*
:   Text for the revision markers.

*bAppendResult*
:   If set to true, already existing comparison results in project are not deleted.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred when comparing projects. |

Remarks

Used for property comparison.
