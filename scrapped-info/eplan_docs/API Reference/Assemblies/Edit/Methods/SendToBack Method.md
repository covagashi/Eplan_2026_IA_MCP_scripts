# SendToBack Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~SendToBack.html

---

Opens the page, selects the Placement passed as oPlacementToMove and move the Placement back.

Syntax

**C#**



public void SendToBack( 

   Placement oPlacementToMove

)

public:

void SendToBack( 

   Placement^ oPlacementToMove

)


#### Parameters

*oPlacementToMove*
:   Placement to move.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Is thrown in case of NULL parameters. |
| [System.ApplicationException](#) | The graphics editor interface could not be created. |
