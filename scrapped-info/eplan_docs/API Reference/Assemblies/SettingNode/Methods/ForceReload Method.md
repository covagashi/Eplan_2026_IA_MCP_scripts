# ForceReload Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SettingNode~ForceReload.html

---

Reloads settings node.

Syntax

**C#**



public void ForceReload()

public:

void ForceReload();


Exceptions

| Exception | Description |
| --- | --- |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The object has not been initialized correctly. |

Remarks

Changes in settings made from one instance of EPLAN are not visible to other currently running instances. Method allows to reload setting node to get current setting values.
