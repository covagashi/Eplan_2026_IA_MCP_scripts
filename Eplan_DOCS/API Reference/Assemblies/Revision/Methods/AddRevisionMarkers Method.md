# AddRevisionMarkers Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~AddRevisionMarkers.html

---

Adds revision markers to the changed project. Used for change tracking.

Syntax

**C#**



public void AddRevisionMarkers( 

   Project oProject,

   string strRevisionMarker

)

public:

void AddRevisionMarkers( 

   Project^ oProject,

   String^ strRevisionMarker

)


#### Parameters

*oProject*
:   The project to which the markers will be added.

*strRevisionMarker*
:   Text for the marker.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred when adding revision markers. |

Remarks

Used for change tracking.
