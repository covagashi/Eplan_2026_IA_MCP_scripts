# GetMultiLangStringDefault Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetMultiLangStringDefault.html

---

Returns default MultiLangString value of a setting. The index starts at 0.

Syntax

**C#**



public MultiLangString GetMultiLangStringDefault( 

   string strSettingPath,

   int nIdx

)

public:

MultiLangString^ GetMultiLangStringDefault( 

   String^ strSettingPath,

   int nIdx

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

*nIdx*
:   Indicates the index.

#### Return Value

Default MultiLangString value

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
