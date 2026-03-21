# GetNumericSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetNumericSetting.html

---

Reads numeric value from settings. It can be 16 bit or 32 bit, signed or unsigned setting.

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
:   0-based index.

#### Return Value

value read from settings

Exceptions

| Exception | Description |
| --- | --- |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the value cannot be read from settings |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [System.ArgumentException](#) | Thrown when setting path dosn't exist. |
