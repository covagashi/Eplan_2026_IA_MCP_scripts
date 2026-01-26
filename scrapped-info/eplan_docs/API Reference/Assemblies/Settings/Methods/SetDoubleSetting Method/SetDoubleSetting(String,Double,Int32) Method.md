# SetDoubleSetting(String,Double,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~SetDoubleSetting(String,Double,Int32).html

---

Sets the value of a setting. If a setting is made and an index is specified that exceeds the number of values, the corresponding values are created, based on the predefined value. The index starts at 0.

Syntax

**C#**



public virtual void SetDoubleSetting( 

   string strSettingPath,

   double dValue,

   int nIdx

)

public:

virtual void SetDoubleSetting( 

   String^ strSettingPath,

   double dValue,

   int nIdx

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

*dValue*
:   Indicates the value of the setting.

*nIdx*
:   Indicates the index.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when setting cannot be set. |

Remarks

Warning: double values are stored with precision to 15 digits only!
