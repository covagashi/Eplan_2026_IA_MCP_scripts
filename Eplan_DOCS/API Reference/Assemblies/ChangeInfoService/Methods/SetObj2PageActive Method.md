# SetObj2PageActive Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~SetObj2PageActive.html

---

Activate or deactivate change info handling if object belongs to page. Helper will switch mode automatically back due to destruction.

Syntax

**C#**



public void SetObj2PageActive( 

   bool bActive,

   ChangeInfoService.ChangeInfoServiceHelper pHelper

)

public:

void SetObj2PageActive( 

   bool bActive,

   ChangeInfoService.ChangeInfoServiceHelper^ pHelper

)


#### Parameters

*bActive*
:   If true, change info handling is activated.

*pHelper*
:   Object which will switch mode back due to destruction. Can be null value.
