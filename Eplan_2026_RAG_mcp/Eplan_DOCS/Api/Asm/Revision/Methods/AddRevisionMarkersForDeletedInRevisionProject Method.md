# AddRevisionMarkersForDeletedInRevisionProject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~AddRevisionMarkersForDeletedInRevisionProject.html

---

Adds the revision markers of all deleted objects in the comparison project. Note: The comparison project has to be writable. Used for change tracking.

Syntax

**C#**



public void AddRevisionMarkersForDeletedInRevisionProject( 

   Project oComparisonProject,

   Project oProject,

   string strRevisionMarker

)

public:

void AddRevisionMarkersForDeletedInRevisionProject( 

   Project^ oComparisonProject,

   Project^ oProject,

   String^ strRevisionMarker

)


#### Parameters

*oComparisonProject*
:   The comparison project to which the markers for deleted objects will be added.

*oProject*
:   The project containing the comparison results.

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
