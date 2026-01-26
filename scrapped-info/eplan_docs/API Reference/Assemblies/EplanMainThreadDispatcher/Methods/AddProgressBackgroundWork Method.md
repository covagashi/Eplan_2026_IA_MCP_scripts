# AddProgressBackgroundWork Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Internal.EplanMainThreadDispatcher~AddProgressBackgroundWork.html

---

Allows the user to add a progress bar when main thread is working.

Syntax

**C#**



public void AddProgressBackgroundWork( 

   Progress pProgress,

   BackgroundProgressWorkDelegate workDelegate

)

public:

void AddProgressBackgroundWork( 

   Progress^ pProgress,

   BackgroundProgressWorkDelegate^ workDelegate

)


#### Parameters

*pProgress*
:   The Progress at work.

*workDelegate*
:   The work to be done.
