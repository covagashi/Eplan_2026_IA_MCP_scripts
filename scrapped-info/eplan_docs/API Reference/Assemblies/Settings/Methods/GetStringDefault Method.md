# GetStringDefault Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetStringDefault.html

---

Returns default string value of a setting. The index starts at 0.

Syntax

**C#**



public string GetStringDefault( 

   string strSettingPath,

   int nIdx

)

public:

String^ GetStringDefault( 

   String^ strSettingPath,

   int nIdx

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

*nIdx*
:   Indicates the index.

#### Return Value

Default string value

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
