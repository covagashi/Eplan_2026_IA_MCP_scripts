# ClearSetting(String,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~ClearSetting(String,Int32).html

---

Deletes the value. The setting definition is maintained.

Syntax

**C#**



public virtual void ClearSetting( 

   string strSettingPath,

   int idx

)

public:

virtual void ClearSetting( 

   String^ strSettingPath,

   int idx

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting (relative to path of the node, path starts after the path of the node).

*idx*
:   Indicates index of the value of the setting.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | The value of the parameter object is NULL. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The object has not been initialized correctly. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The function failed. |
