# SetBoolSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings~SetBoolSetting.html

---

Sets the value of settings on a given path.

Syntax

**C#**



void SetBoolSetting( 

   string strSettingPath,

   bool bValue,

   int nIdx

)

void SetBoolSetting( 

   String^ strSettingPath,

   bool bValue,

   int nIdx

)


#### Parameters

*strSettingPath*
:   path to settings

*bValue*
:   value to set.

*nIdx*
:   0-based index of the setting

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingsPath` is `null`. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the value cannot be set. |
