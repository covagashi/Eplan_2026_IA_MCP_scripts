# AddStringSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~AddStringSetting.html

---

Defines a new setting for a string value.

Syntax

**C#**



public void AddStringSetting( 

   string strSettingPath,

   string[] arrValues,

   string[] arrRange,

   ISettings.CreationFlag eFlag

)

public:

void AddStringSetting( 

   String^ strSettingPath,

   array<String^>^ arrValues,

   array<String^>^ arrRange,

   ISettings.CreationFlag eFlag

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

*arrValues*
:   Array of values added to the setting

*arrRange*
:   Ranges used for value validation.

*eFlag*
:   [ISettings.CreationFlag](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings+CreationFlag.html)

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when setting cannot be added. |

Remarks

Default definition settings are provided for settings that use default values such as FALSE, TRUE, 0, or spaces and that do not require ranges of values.
