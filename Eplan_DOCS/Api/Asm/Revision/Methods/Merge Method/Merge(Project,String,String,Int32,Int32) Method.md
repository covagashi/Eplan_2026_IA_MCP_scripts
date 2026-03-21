# Merge(Project,String,String,Int32,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~Merge(Project,String,String,Int32,Int32).html

---

Unites project revisions. Used for change tracking.

Syntax

**C#**



public void Merge( 

   Project oProj,

   string strRevisionName,

   string strComment,

   int nProjectRevisionIndexFrom,

   int nProjectRevisionIndexTo

)

public:

void Merge( 

   Project^ oProj,

   String^ strRevisionName,

   String^ strComment,

   int nProjectRevisionIndexFrom,

   int nProjectRevisionIndexTo

)


#### Parameters

*oProj*
:   Project to unite revisions

*strRevisionName*
:   Name of the new united project revision

*strComment*
:   Comment of the new united project revision (optional)

*nProjectRevisionIndexFrom*
:   Project revision index to start with unification. Corresponds to index of project property PROJ\_REVISION\_LOG\_NAME which holds revision names.

*nProjectRevisionIndexTo*
:   Project revision index to end with unification. Corresponds to index of project property PROJ\_REVISION\_LOG\_NAME which holds revision names.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the action. |

Remarks

Used for change tracking. When a revision for a project section is active, only the revisions of the project section is united.
