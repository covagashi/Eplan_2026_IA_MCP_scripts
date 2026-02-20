# ExistSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~ExistSetting.html

---

Check if there exist a setting on path given as a parameter.

Syntax

**C#**



public virtual bool ExistSetting( 

   string strSettingPath

)

public:

virtual bool ExistSetting( 

   String^ strSettingPath

)


#### Parameters

*strSettingPath*
:   path to project settings

#### Return Value

bool indicating if the setting exist

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingsPath` is `null`. |
