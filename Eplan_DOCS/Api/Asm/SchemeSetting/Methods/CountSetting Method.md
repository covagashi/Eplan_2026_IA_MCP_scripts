# CountSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~CountSetting.html

---

Number of additional settings existing under the specified setting name.

Syntax

**C#**



public int CountSetting( 

   string strSettingPath

)

public:

int CountSetting( 

   String^ strSettingPath

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting (relative to scheme, path starts after scheme name).

#### Return Value

Number of indexed settings of this setting in the scheme.
