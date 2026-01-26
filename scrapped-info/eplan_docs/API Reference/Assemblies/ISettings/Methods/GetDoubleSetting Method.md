# GetDoubleSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings~GetDoubleSetting.html

---

Reads double value from settings

Syntax

**C#**



double GetDoubleSetting( 

   string strSettingPath,

   int nIdx

)

double GetDoubleSetting( 

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
| [System.ArgumentNullException](#) | Thrown when `strSettingsPath` is `null`. |
| [System.ArgumentException](#) | Thrown when setting path dosn't exist. |

Remarks

Warning: double values are stored with precision to 15 digits only!
