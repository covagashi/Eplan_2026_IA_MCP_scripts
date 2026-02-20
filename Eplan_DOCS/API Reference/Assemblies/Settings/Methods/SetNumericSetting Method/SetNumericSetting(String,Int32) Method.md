# SetNumericSetting(String,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~SetNumericSetting(String,Int32).html

---

Sets the value of a setting. The index under which setting will be written is evaluated automatically. First free index is used. The index starts at 0.

Syntax

**C#**



public void SetNumericSetting( 

   string strSettingPath,

   int nValue

)

public:

void SetNumericSetting( 

   String^ strSettingPath,

   int nValue

)


#### Parameters

*strSettingPath*
:   path to settings

*nValue*
:   value to set.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when setting cannot be set. |
