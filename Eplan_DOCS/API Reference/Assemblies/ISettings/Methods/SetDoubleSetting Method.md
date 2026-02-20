# SetDoubleSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings~SetDoubleSetting.html

---

Sets the value of settings on a given path.

Syntax

**C#**



void SetDoubleSetting( 

   string strSettingPath,

   double dValue,

   int nIdx

)

void SetDoubleSetting( 

   String^ strSettingPath,

   double dValue,

   int nIdx

)


#### Parameters

*strSettingPath*
:   path to settings

*dValue*
:   value to set.

*nIdx*
:   0-based index of the setting

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingsPath` is `null`. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the value cannot be set. |

Remarks

Warning: double values are stored with precision to 15 digits only!
