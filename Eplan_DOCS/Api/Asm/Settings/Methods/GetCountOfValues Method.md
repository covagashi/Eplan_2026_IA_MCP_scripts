# GetCountOfValues Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetCountOfValues.html

---

Returnes the number of values of a setting.

Syntax

**C#**



public int GetCountOfValues( 

   string strSettingPath

)

public:

int GetCountOfValues( 

   String^ strSettingPath

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

#### Return Value

The number of values of the setting, as unsigned integer.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The setting is not defined. |
