# AddDoubleSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~AddDoubleSetting.html

---

Defines a new setting for a double value.

Syntax

**C#**



public void AddDoubleSetting( 

   string strSettingPath,

   double[] arrValues,

   Range[] arrRange,

   ISettings.CreationFlag eFlag

)

public:

void AddDoubleSetting( 

   String^ strSettingPath,

   array<double>^ arrValues,

   array<Range^>^ arrRange,

   ISettings.CreationFlag eFlag

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

*arrValues*
:   Array of values added to the setting

*arrRange*
:   Array of [Range](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Range.html). Used for value validation.

*eFlag*
:   [ISettings.CreationFlag](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings+CreationFlag.html)

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when setting cannot be added. |

Remarks

Default definition settings are provided for settings that use default values such as FALSE, TRUE, 0, or spaces and that do not require ranges of values. Warning: double values are stored with precision to 15 digits only!
