# BringToFront Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~BringToFront.html

---

Opens the page, selects the Placement passed as oPlacementToMove and move the Placement front.

Syntax

**C#**



public void BringToFront( 

   Placement oPlacementToMove

)

public:

void BringToFront( 

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
