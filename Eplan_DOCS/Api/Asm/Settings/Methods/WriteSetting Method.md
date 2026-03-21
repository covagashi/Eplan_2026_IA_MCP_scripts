# WriteSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~WriteSetting.html

---

Exports the specified setting to an XML file.

Syntax

**C#**



public void WriteSetting( 

   string strSettingPath,

   string strFilename

)

public:

void WriteSetting( 

   String^ strSettingPath,

   String^ strFilename

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

*strFilename*
:   Indicates the full file name of the settings XML file.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. Thrown when `strFilename` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. Thrown when `strFilename` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The setting is not defined. |
