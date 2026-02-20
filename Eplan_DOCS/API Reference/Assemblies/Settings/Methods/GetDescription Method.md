# GetDescription Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetDescription.html

---

\Returns the description of a setting.

Syntax

**C#**



public string GetDescription( 

   string strSettingPath

)

public:

String^ GetDescription( 

   String^ strSettingPath

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

#### Return Value

The description of a setting as a string.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The setting is not defined. |
