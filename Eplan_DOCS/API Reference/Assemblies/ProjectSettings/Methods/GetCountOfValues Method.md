# GetCountOfValues Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSettings~GetCountOfValues.html

---

Returnes the count of indexed values that are used already by the project setting.

Syntax

**C#**



public int GetCountOfValues( 

   string strSettingPath

)

public:

int GetCountOfValues( 

   String^ strSettingPath

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting

#### Return Value

The number of values of the setting.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty or specified setting doesn't exist. |
