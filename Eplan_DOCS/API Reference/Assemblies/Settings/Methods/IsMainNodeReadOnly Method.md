# IsMainNodeReadOnly Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Settings~IsMainNodeReadOnly.html

---

Verifies whether the main node (COMPANY / STATION / USER) of the specified setting is Readonly.

Syntax

**C#**



public bool IsMainNodeReadOnly( 

   string strSettingPath

)

public:

bool IsMainNodeReadOnly( 

   String^ strSettingPath

)


#### Parameters

*strSettingPath*
:   Indicates the path of the setting.

#### Return Value

Boolean value that indicates whether the main node is Readonly.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strSettingPath` is `null`. |
| [System.ArgumentException](#) | Thrown when `strSettingPath` is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Method failed. |
