# AddMultiLangStringSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~AddMultiLangStringSetting.html

---

Defines a new setting for a multilanguage string value.

Syntax

**C#**



public void AddMultiLangStringSetting( 

   string strSettingPath,

   MultiLangString[] arrValues,

   MultiLangString[] arrRange,

   ISettings.CreationFlag eFlag

)

public:

void AddMultiLangStringSetting( 

   String^ strSettingPath,

   array<MultiLangString^>^ arrValues,

   array<MultiLangString^>^ arrRange,

   ISettings.CreationFlag eFlag

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting

*arrValues*
:   Array of values added to the setting

*arrRange*
:   Ranges used for value validation

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
