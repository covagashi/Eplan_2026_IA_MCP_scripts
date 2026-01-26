# RemoveScheme Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~RemoveScheme.html

---

Remove a new scheme.

Syntax

**C#**



public void RemoveScheme( 

   string strSettingsNodeName

)

public:

void RemoveScheme( 

   String^ strSettingsNodeName

)


#### Parameters

*strSettingsNodeName*
:   The node name in the settings

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when a parameter is `null`. |
| [System.ArgumentException](#) | Thrown when a parameter is empty. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when strName is not a valid last used scheme.The scheme with this strSettingsNodeName does not exist. |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The scheme has only one more scheme left. The last one is not allowed to delete. |

Remarks

A read-only scheme cannot be deleted.
