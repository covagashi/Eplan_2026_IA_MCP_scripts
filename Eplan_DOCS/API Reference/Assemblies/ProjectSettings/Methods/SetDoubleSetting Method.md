# SetDoubleSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~SetDoubleSetting.html

---

Sets the value of a project setting in a specified path.

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
:   Path to the project setting

*dValue*
:   Value to be set

*nIdx*
:   0-based index of the setting

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if the `strSettingsPath` parameter is `NULL`. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if the value cannot be set. |

Remarks

Warning: double values are stored with precision to 15 digits only!
