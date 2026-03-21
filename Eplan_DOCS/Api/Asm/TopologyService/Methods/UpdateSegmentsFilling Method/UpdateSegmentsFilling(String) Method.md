# UpdateSegmentsFilling(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TopologyService~UpdateSegmentsFilling(String).html

---

Calculates and sets value of property CABLINGSEGMENT\_FILLING for all segments in project.

Syntax

**C#**



public bool UpdateSegmentsFilling( 

   string strFullLinkFileName

)

public:

bool UpdateSegmentsFilling( 

   String^ strFullLinkFileName

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project, which contains the page to export.

#### Return Value

`True` if no propblem was found during calculation.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | If parameter is `null`. |
| [System.ArgumentException](#) | If project not exists. |
