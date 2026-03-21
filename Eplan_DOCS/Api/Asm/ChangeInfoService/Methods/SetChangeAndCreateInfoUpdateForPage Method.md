# SetChangeAndCreateInfoUpdateForPage Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~SetChangeAndCreateInfoUpdateForPage.html

---

Activate or deactivate automatic change/create information update for a page. Helper will switch mode automatically back due to destruction.

Syntax

**C#**



public void SetChangeAndCreateInfoUpdateForPage( 

   bool bChandeAndCreateInfoUpdate,

   ChangeInfoService.ChangeInfoServiceHelper pHelper

)

public:

void SetChangeAndCreateInfoUpdateForPage( 

   bool bChandeAndCreateInfoUpdate,

   ChangeInfoService.ChangeInfoServiceHelper^ pHelper

)


#### Parameters

*bChandeAndCreateInfoUpdate*
:   If true, automatic change/create information update for a page is activated.

*pHelper*
:   Object which will switch mode back due to destruction. Can be null value.
