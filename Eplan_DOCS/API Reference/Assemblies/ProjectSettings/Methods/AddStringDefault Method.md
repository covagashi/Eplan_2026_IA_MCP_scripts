# AddStringDefault Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~AddStringDefault.html

---

Defines a new setting for a string default.

Syntax

**C#**



public void AddStringDefault( 

   string strSettingPath,

   string[] arrDefaults,

   string[] arrRange,

   ISettings.CreationFlag eFlag

)

public:

void AddStringDefault( 

   String^ strSettingPath,

   array<String^>^ arrDefaults,

   array<String^>^ arrRange,

   ISettings.CreationFlag eFlag

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

*arrDefaults*
:   Array of default values

*arrRange*
:   Ranges used for value validation.

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
