# DeleteSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~DeleteSetting.html

---

Resets a setting to the value from the default settings. If the setting has no default value, it will be deleted.

Syntax

**C#**



public void DeleteSetting( 

   string strSettingPath

)

public:

void DeleteSetting( 

   String^ strSettingPath

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when setting cannot be reset. |
