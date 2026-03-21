# SetConnectionDirtyActive Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeInfoService~SetConnectionDirtyActive.html

---

Activate or deactivate connection dirty bit handling. Helper will switch mode automatically back due to destruction.

Syntax

**C#**



public void SetConnectionDirtyActive( 

   bool bActive,

   ChangeInfoService.ChangeInfoServiceHelper pHelper

)

public:

void SetConnectionDirtyActive( 

   bool bActive,

   ChangeInfoService.ChangeInfoServiceHelper^ pHelper

)


#### Parameters

*bActive*
:   If true, connection dirty bit handling is activated.

*pHelper*
:   Object which will switch mode back due to destruction. Can be null value.
