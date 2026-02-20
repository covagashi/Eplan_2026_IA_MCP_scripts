# RemoveWriteProtection Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~RemoveWriteProtection.html

---

Removes write protection on a project (i.e. opens the current revision for changes). Used for change tracking.

Syntax

**C#**



public void RemoveWriteProtection( 

   Project oProject

)

public:

void RemoveWriteProtection( 

   Project^ oProject

)


#### Parameters

*oProject*
:   A project to take the action on.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the action. |

Remarks

Used for change tracking. When a revision for a project section is active, only the pages and installation spaces of this project section are included. This pages and installation spaces are writable afterwards.
