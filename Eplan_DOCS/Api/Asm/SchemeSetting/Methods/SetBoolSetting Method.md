# SetBoolSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetBoolSetting.html

---

Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0.

Syntax

**C#**



public void SetBoolSetting( 

   string strSettingPath,

   bool value,

   int nIdx

)

public:

void SetBoolSetting( 

   String^ strSettingPath,

   bool value,

   int nIdx

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting (relative to scheme, path starts after scheme name).

*value*
:   Indicates the value of the setting.

*nIdx*
:   Indicates the index.
