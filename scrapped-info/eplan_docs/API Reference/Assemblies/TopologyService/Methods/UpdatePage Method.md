# UpdatePage Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TopologyService~UpdatePage.html

---

Updates start and end position of all segment elements found on a page.

Syntax

**C#**



public void UpdatePage( 

   Page pPage

)

public:

void UpdatePage( 

   Page^ pPage

)


#### Parameters

*pPage*
:   [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) on which segments will be updated.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Parameter `pPage` was set to `null`. |
| [System.ArgumentException](#) | If parameter is invalid. |
| [System.ApplicationException](#) | Failed to update the page. Please refer to the error message. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An internal error occurred during update. Please refer to the error message. |

Remarks

Method sets correct start and end positions for each found [Eplan.EplApi.DataModel.Topology.Segment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.Segment.html). A position on one site of segment is updated only if a [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html) is assigned to this side.

If this method will find more then just one segment which connect same two devices, it will remove duplicated segments and leave only one.
