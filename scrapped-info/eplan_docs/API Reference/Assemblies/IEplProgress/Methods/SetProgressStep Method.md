# SetProgressStep Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.IEplProgress~SetProgressStep.html

---

The actual stepping of the progress. The function is called for every level the progress supports.

Syntax

**C#**



void SetProgressStep( 

   int nLevel,

   int nSpent

)

void SetProgressStep( 

   int nLevel,

   int nSpent

)


#### Parameters

*nLevel*
:   1 to GetLevelCount + 1. 1 is the overall progress

*nSpent*
:   Contains the new value the progress should show. Is always between 0 and 100.
