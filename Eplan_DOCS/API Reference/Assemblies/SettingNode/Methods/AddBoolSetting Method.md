# AddBoolSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~AddBoolSetting.html

---

Defines a new setting for a boolean value.

Syntax

**C#**



public void AddBoolSetting( 

   string strSettingPath,

   bool[] arrValues,

   ISettings.CreationFlag eFlag

)

public:

void AddBoolSetting( 

   String^ strSettingPath,

   array<bool>^ arrValues,

   ISettings.CreationFlag eFlag

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting (relative to path of the node, path starts after the path of the node).

*arrValues*
:   Array of values added to the setting

*eFlag*
:   [ISettings.CreationFlag](Eplan.EplApi.Baseu~Eplan.EplApi.Base.ISettings+CreationFlag.html)

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [System.ArgumentNullException](#) | Thrown when `strDefBy` is `null`. |
| [System.ArgumentException](#) | Thrown when `strDefBy` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when setting cannot be added. |

Remarks

Default definition settings are provided for settings that use default values such as FALSE, TRUE, 0, or spaces and that do not require ranges of values.
