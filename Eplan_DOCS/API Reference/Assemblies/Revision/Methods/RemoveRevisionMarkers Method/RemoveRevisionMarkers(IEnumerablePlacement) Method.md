# RemoveRevisionMarkers(IEnumerable<Placement>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~RemoveRevisionMarkers(IEnumerable{Placement}).html

---

Removes revision marker. Used for change tracking.

Syntax

**C#**



public void RemoveRevisionMarkers( 

   IEnumerable<Placement> colPlacements

)

public:

void RemoveRevisionMarkers( 

   IEnumerable<Placement^>^ colPlacements

)


#### Parameters

*colPlacements*
:   Placements for which revision markers will be removed.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the action. |

Remarks

Used for change tracking. When a revision for a project section is active, only the markers of the pages and installation spaces are included.
