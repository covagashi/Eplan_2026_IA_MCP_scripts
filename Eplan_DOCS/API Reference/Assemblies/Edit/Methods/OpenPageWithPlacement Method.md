# OpenPageWithPlacement Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~OpenPageWithPlacement.html

---

Opens the page and selects the Placement passed as oPlacementToSelect. The Placement is selected in the graphic editor.

Syntax

**C#**



public void OpenPageWithPlacement( 

   Placement oPlacementToSelect

)

public:

void OpenPageWithPlacement( 

   Placement^ oPlacementToSelect

)


#### Parameters

*oPlacementToSelect*
:   Placement to be selected.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Is thrown in case of NULL parameters. |
| [System.ApplicationException](#) | The graphics editor interface could not be created. |
