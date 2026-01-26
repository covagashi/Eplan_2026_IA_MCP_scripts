# EndPartCalled Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.IEplProgress~EndPartCalled.html

---

One progress part ends. Perhaps you want to set a new actiontext for this part!

Syntax

**C#**



void EndPartCalled( 

   int nNewLevel,

   string strActionText

)

void EndPartCalled( 

   int nNewLevel,

   String^ strActionText

)


#### Parameters

*nNewLevel*
:   which part is started.

*strActionText*
:   the new action text for this part.
