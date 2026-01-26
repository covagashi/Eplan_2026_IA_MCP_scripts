# RemoveRevisionData(IEnumerable<Placement>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~RemoveRevisionData(IEnumerable{Placement}).html

---

Removes revision data from placements. Used for change tracking.

Syntax

**C#**



public void RemoveRevisionData( 

   IEnumerable<Placement> colPlacements

)

public:

void RemoveRevisionData( 

   IEnumerable<Placement^>^ colPlacements

)


#### Parameters

*colPlacements*
:   Placements.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the action. |

Remarks

Used for change tracking.
