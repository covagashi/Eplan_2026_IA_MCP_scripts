# AddNumericDefault Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~AddNumericDefault.html

---

Defines a new setting for a numeric default.

Syntax

**C#**



public void AddNumericDefault( 

   string strSettingPath,

   int[] arrDefaults,

   Range[] arrRange,

   ISettings.CreationFlag eFlag

)

public:

void AddNumericDefault( 

   String^ strSettingPath,

   array<int>^ arrDefaults,

   array<Range^>^ arrRange,

   ISettings.CreationFlag eFlag

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

*arrDefaults*
:   Array of default values

*arrRange*
:   Array of [Eplan.EplApi.Base.Range](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Range.html). Used for value validation.

*eFlag*
:   [Eplan.EplApi.Base.ISettings.CreationFlag](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings+CreationFlag.html)

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when setting cannot be added. |

Remarks

Default definition settings are provided for settings that use default values such as FALSE, TRUE, 0, or spaces and that do not require ranges of values.
