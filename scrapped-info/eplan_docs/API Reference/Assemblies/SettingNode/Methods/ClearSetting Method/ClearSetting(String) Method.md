# ClearSetting(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~ClearSetting(String).html

---

Deletes values. The setting definition is maintained.

Syntax

**C#**



public virtual void ClearSetting( 

   string strSettingPath

)

public:

virtual void ClearSetting( 

   String^ strSettingPath

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting (relative to path of the node, path starts after the path of the node).

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | The value of the parameter object is NULL. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The object has not been initialized correctly. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The function failed. |
