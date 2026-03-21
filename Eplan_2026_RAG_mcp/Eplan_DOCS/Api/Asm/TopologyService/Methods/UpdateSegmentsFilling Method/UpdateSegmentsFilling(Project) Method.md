# UpdateSegmentsFilling(Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TopologyService~UpdateSegmentsFilling(Project).html

---

Calculates and sets value of property CABLINGSEGMENT\_FILLING for all segments in project.

Syntax

**C#**



public bool UpdateSegmentsFilling( 

   Project pProject

)

public:

bool UpdateSegmentsFilling( 

   Project^ pProject

)


#### Parameters

*pProject*
:   [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) for which calculation will be done.

#### Return Value

`True` if no propblem was found during calculation.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | If any parameter is `null`. |
| [System.ArgumentException](#) | If any parameter is invalid. |
