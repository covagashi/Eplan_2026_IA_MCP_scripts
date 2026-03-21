# SetStringSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetStringSetting.html

---

Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0.

Syntax

**C#**



public void SetStringSetting( 

   string strSettingPath,

   string strvalue,

   int nIdx

)

public:

void SetStringSetting( 

   String^ strSettingPath,

   String^ strvalue,

   int nIdx

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting (relative to scheme, path starts after scheme name).

*strvalue*
:   Indicates the value of the setting.

*nIdx*
:   Indicates the index.
