# ExistSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~ExistSetting.html

---

Verifies whether specified setting exists.

Syntax

**C#**



public virtual bool ExistSetting( 

   string strSettingPath

)

public:

virtual bool ExistSetting( 

   String^ strSettingPath

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

#### Return Value

Boolean value that indicates whether setting exists.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Method failed. |
