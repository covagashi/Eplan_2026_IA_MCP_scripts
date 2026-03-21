# UpdateTopologySegment Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TopologyService~UpdateTopologySegment.html

---

Updates start and end position of a segment.

Syntax

**C#**



public void UpdateTopologySegment( 

   Segment pSegment

)

public:

void UpdateTopologySegment( 

   Segment^ pSegment

)


#### Parameters

*pSegment*
:   [Eplan.EplApi.DataModel.Topology.Segment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.Segment.html) which will be updated.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Parameter `pSegment` was set to `null`. |
| [System.ArgumentException](#) | If parameter is invalid. |
| [System.ApplicationException](#) | Failed to update the segment. Please refer to the error message. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An internal error occurred during update. Please refer to the error message. |

Remarks

Method sets correct start and end positions for a [Eplan.EplApi.DataModel.Topology.Segment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.Segment.html). A position on one site of segment is updated only if a [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html) is assigned to this side.
