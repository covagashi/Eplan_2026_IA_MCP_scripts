# GetTypeOfSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetTypeOfSetting.html

---

Returns the type of the setting.

Syntax

**C#**



public virtual ISettings.SettingType GetTypeOfSetting( 

   string strSettingPath

)

public:

virtual ISettings.SettingType GetTypeOfSetting( 

   String^ strSettingPath

)


#### Parameters

*strSettingPath*
:   path to settings

#### Return Value

the type of the setting as enum

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingsPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The setting is not defined. |
