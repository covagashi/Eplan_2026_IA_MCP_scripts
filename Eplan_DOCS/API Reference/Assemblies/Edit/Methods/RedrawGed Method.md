# RedrawGed Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~RedrawGed.html

---

Redraws GED surface.

Syntax

**C#**



public bool RedrawGed()

public:

bool RedrawGed();


#### Return Value

TRUE if operation succeeded and FALSE if not.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ApplicationException](#) | The graphics editor interface could not be created. |

Remarks

GED is not redrawn when Eplan P8 is opened in 'Quiet' mode. In this case method call always returns FALSE.
