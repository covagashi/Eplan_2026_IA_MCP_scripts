# RemoveAllIndexedSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~RemoveAllIndexedSetting.html

---

Removes all indexed setting.

Syntax

**C#**



public void RemoveAllIndexedSetting( 

   string strSetting

)

public:

void RemoveAllIndexedSetting( 

   String^ strSetting

)


#### Parameters

*strSetting*
:   Indicates the path of the setting.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when setting cannot be removed. |
