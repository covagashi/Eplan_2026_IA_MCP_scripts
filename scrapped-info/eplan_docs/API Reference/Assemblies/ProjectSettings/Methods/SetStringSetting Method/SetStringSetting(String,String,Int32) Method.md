# SetStringSetting(String,String,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~SetStringSetting(String,String,Int32).html

---

Sets the value of a project setting in a specified path.

Syntax

**C#**



public virtual void SetStringSetting( 

   string strSettingPath,

   string strValue,

   int nIdx

)

public:

virtual void SetStringSetting( 

   String^ strSettingPath,

   String^ strValue,

   int nIdx

)


#### Parameters

*strSettingPath*
:   Path to the project setting

*strValue*
:   Value to be set

*nIdx*
:   0-based index of the setting

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if the `strSettingsPath` parameter is `NULL`. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if the value cannot be set. |
