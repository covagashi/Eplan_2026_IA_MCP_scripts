# GetNumericSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~GetNumericSetting.html

---

Reads numeric value from settings. It can be 16 bit or 32 bit, signed or unsigned setting.

Syntax

**C#**



public int GetNumericSetting( 

   string strSettingPath,

   int nIdx

)

public:

int GetNumericSetting( 

   String^ strSettingPath,

   int nIdx

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting (relative to scheme, path starts after scheme name).

*nIdx*
:   0-based index.

#### Return Value

value read from settings

Exceptions

| Exception | Description |
| --- | --- |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the value cannot be read from settings |
| [System.ArgumentNullException](#) | Thrown when `strSettingsPath` is `null`. |
