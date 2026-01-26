# SetStringSetting(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~SetStringSetting(String,String).html

---

Sets the value of a project setting in a specified path to the first free index.

Syntax

**C#**



public virtual void SetStringSetting( 

   string strSettingPath,

   string strValue

)

public:

virtual void SetStringSetting( 

   String^ strSettingPath,

   String^ strValue

)


#### Parameters

*strSettingPath*
:   Path to the project setting

*strValue*
:   Value to be set

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if the `strSettingsPath` parameter is `NULL`. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if the value cannot be set. |
