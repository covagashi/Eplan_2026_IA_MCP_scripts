# Merge(Project,String,String,Int32[]) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~Merge(Project,String,String,Int32[]).html

---

Unites project revisions. Used for change tracking.

Syntax

**C#**



public void Merge( 

   Project oProj,

   string strRevisionName,

   string strComment,

   int[] nProjectRevisionIndices

)

public:

void Merge( 

   Project^ oProj,

   String^ strRevisionName,

   String^ strComment,

   array<int>^ nProjectRevisionIndices

)


#### Parameters

*oProj*
:   Project to unite revisions

*strRevisionName*
:   Name of the new united project revision

*strComment*
:   Comment of the new united project revision (optional)

*nProjectRevisionIndices*
:   Project revision index to unite.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the action. |

Remarks

Used for change tracking. When a revision for a project section is active, only the revisions of the project section is united.
