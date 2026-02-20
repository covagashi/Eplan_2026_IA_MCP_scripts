# GetBoolDefault Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetBoolDefault.html

---

Returns default boolean value of a setting. The index starts at 0.

Syntax

**C#**



public bool GetBoolDefault( 

   string strSettingPath,

   int nIdx

)

public:

bool GetBoolDefault( 

   String^ strSettingPath,

   int nIdx

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

*nIdx*
:   Indicates the index.

#### Return Value

Default bool value

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
