# GetExpandedStringSetting Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetExpandedStringSetting.html

---

Returns the value of a string setting. If a setting is read that has no value for this index, the default value is returned. The index starts at 0. If this path is identified via an EPLAN path (e.g. $Eplan, $MD, ...) this identifier is resolved.

Syntax

**C#**



public virtual string GetExpandedStringSetting( 

   string strSettingPath,

   int nIdx

)

public:

virtual String^ GetExpandedStringSetting( 

   String^ strSettingPath,

   int nIdx

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

*nIdx*
:   Indicates the index.

#### Return Value

Returns the value of the setting.

Exceptions

| Exception | Description |
| --- | --- |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The setting is not defined. |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [System.ArgumentException](#) | Thrown when setting path dosn't exist. |
