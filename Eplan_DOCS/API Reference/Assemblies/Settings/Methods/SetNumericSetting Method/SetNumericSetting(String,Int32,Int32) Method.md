# SetNumericSetting(String,Int32,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~SetNumericSetting(String,Int32,Int32).html

---

Sets the value of settings on a given path. Type of value will be converted to 16 bit, 32 bit, signed or unsigned value depending on setting type.

Syntax

**C#**



public virtual void SetNumericSetting( 

   string strSettingPath,

   int nValue,

   int nIdx

)

public:

virtual void SetNumericSetting( 

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
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when setting cannot be set. |
