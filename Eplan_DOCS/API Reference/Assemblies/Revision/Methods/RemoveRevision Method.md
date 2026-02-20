# RemoveRevision Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~RemoveRevision.html

---

Deletes last revision. Used for change tracking.

Syntax

**C#**



public void RemoveRevision( 

   Project oProject

)

public:

void RemoveRevision( 

   Project^ oProject

)


#### Parameters

*oProject*
:   A project to take the action on. Project cannot be read-only. There must be at least 2 revisions in the project.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the action. |

Remarks

Used for change tracking.
