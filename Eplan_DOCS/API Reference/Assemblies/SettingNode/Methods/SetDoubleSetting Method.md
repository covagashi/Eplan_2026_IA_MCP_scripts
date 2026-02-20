# SetDoubleSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~SetDoubleSetting.html

---

Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0.

Syntax

**C#**



public virtual void SetDoubleSetting( 

   string strSettingPath,

   double value,

   int idx

)

public:

virtual void SetDoubleSetting( 

   String^ strSettingPath,

   double value,

   int idx

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting (relative to path of the node, path starts after the path of the node).

*value*
:   Indicates the value of the setting.

*idx*
:   Indicates the index.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | The value of the parameter object is NULL. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The object has not been initialized correctly. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The function failed. |

Remarks

Precision: 15 numbers of significant digits are supported.
