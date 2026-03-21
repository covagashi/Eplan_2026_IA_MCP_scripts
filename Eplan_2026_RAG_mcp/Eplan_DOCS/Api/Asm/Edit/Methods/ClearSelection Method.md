# ClearSelection Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~ClearSelection.html

---

Removes selection from all objects in the GED.

Syntax

**C#**



public void ClearSelection()

public:

void ClearSelection();


Exceptions

| Exception | Description |
| --- | --- |
| [System.ApplicationException](#) | The graphics editor interface could not be created. |

Remarks

To see in ged that the selection is cleared use [RedrawGed](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~RedrawGed.html) to redraw the GED. Selections in the different navigators will not be removed
