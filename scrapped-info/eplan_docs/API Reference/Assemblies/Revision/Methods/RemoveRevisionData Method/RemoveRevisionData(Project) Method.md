# RemoveRevisionData(Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~RemoveRevisionData(Project).html

---

Removes revision data. Used for change tracking.

Syntax

**C#**



public void RemoveRevisionData( 

   Project oProject

)

public:

void RemoveRevisionData( 

   Project^ oProject

)


#### Parameters

*oProject*
:   A project to take the action on. Project cannot be read-only.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the action. |

Remarks

Used for change tracking.
