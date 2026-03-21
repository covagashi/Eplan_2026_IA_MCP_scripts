# GetMultiLangStringSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~GetMultiLangStringSetting.html

---

Returns the value of a setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0.

Syntax

**C#**



public virtual MultiLangString GetMultiLangStringSetting( 

   string strSettingPath,

   int idx

)

public:

virtual MultiLangString^ GetMultiLangStringSetting( 

   String^ strSettingPath,

   int idx

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting (relative to path of the node, path starts after the path of the node).

*idx*
:   Indicates the index.

#### Return Value

Returns the value of the setting.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | The value of the parameter object is NULL. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The object has not been initialized correctly. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The function failed. |
