# GetBoolSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~GetBoolSetting.html

---

Reads bool value from project settings

Syntax

**C#**



public virtual bool GetBoolSetting( 

   string strSettingPath,

   int nIdx

)

public:

virtual bool GetBoolSetting( 

   String^ strSettingPath,

   int nIdx

)


#### Parameters

*strSettingPath*
:   Path to settings

*nIdx*
:   0\-based index.

#### Return Value

value read from project settings

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the value cannot be read from project settings |
| [System.ArgumentNullException](#) | Thrown when `strSettingsPath` is `null`. |
| [System.ArgumentException](#) | Thrown when setting path doesn't exist. |
