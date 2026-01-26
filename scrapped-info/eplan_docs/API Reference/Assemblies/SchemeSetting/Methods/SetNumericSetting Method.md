# SetNumericSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~SetNumericSetting.html

---

Sets the value of settings on a given path. Type of value will be converted to 16 bit, 32 bit, signed or unsigned value depending on setting type.

Syntax

**C#**



public void SetNumericSetting( 

   string strSettingPath,

   int nValue,

   int nIdx

)

public:

void SetNumericSetting( 

   String^ strSettingPath,

   int nValue,

   int nIdx

)


#### Parameters

*strSettingPath*
:   path to settings

*nValue*
:   value to set.

*nIdx*
:   0-based index of the setting

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingsPath` is `null`. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the value cannot be set. |
