# GetNumericSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~GetNumericSetting.html

---

Reads numeric value from project settings. It can be 16 bit or 32 bit, signed or unsigned setting.

Syntax

**C#**



public virtual int GetNumericSetting( 

   string strSettingPath,

   int nIdx

)

public:

virtual int GetNumericSetting( 

   String^ strSettingPath,

   int nIdx

)


#### Parameters

*strSettingPath*
:   Path to settings

*nIdx*
:   0\-based index.

#### Return Value

value read from settings

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the value cannot be read from settings |
| [System.ArgumentNullException](#) | Thrown when `strSettingsPath` is `null`. |
| [System.ArgumentException](#) | Thrown when setting path doesn't exist. |
