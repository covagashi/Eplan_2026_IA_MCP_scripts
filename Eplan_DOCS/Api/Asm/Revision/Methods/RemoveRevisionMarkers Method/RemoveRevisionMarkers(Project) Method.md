# RemoveRevisionMarkers(Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~RemoveRevisionMarkers(Project).html

---

Removes revision markers from a project. Used for change tracking.

Syntax

**C#**



public void RemoveRevisionMarkers( 

   Project oProject

)

public:

void RemoveRevisionMarkers( 

   Project^ oProject

)


#### Parameters

*oProject*
:   The project in which the markers will be removed.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred when removing revision markers. |

Remarks

Used for change tracking.
