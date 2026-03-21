# SetMultiLangStringSetting(String,MultiLangString) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~SetMultiLangStringSetting(String,MultiLangString).html

---

Sets the value of a setting. The index under which setting will be written is evaluated automatically. First free index is used. The index starts at 0.

Syntax

**C#**



public void SetMultiLangStringSetting( 

   string strSettingPath,

   MultiLangString mlValue

)

public:

void SetMultiLangStringSetting( 

   String^ strSettingPath,

   MultiLangString^ mlValue

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

*mlValue*
:   Indicates the value of the setting.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when setting cannot be set. |
