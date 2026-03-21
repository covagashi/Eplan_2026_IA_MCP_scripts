# SetNumericSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~SetNumericSetting.html

---

Sets the value of a project setting in a specified path. The type of value will be converted to 16 bit, 32 bit, signed or unsigned value depending on the setting type.

Syntax

**C#**



public virtual void SetNumericSetting( 

   string strSettingPath,

   int nValue,

   int nIdx

)

public:

virtual void SetNumericSetting( 

   String^ strSettingPath,

   int nValue,

   int nIdx

)


#### Parameters

*strSettingPath*
:   Path to the project setting

*nValue*
:   Value to be set

*nIdx*
:   0-based index of the setting

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if the `strSettingsPath` parameter is `NULL`. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if the value cannot be set. |
