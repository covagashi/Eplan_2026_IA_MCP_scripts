# GetDoubleDefault Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~GetDoubleDefault.html

---

Returns default double value of a setting. The index starts at 0.

Syntax

**C#**



public double GetDoubleDefault( 

   string strSettingPath,

   int nIdx

)

public:

double GetDoubleDefault( 

   String^ strSettingPath,

   int nIdx

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

*nIdx*
:   Indicates the index.

#### Return Value

Default double value

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |

Remarks

Warning: double values are stored with precision to 15 digits only!
