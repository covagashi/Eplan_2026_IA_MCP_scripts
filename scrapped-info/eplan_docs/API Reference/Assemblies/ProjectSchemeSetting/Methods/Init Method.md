# Init Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSchemeSetting~Init.html

---

Initializes object with a settings node path.

Overload List

| Overload | Description |
| --- | --- |
| [Init(String)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSchemeSetting~Init(String).html) | Initializes object with a settings node path. |
| [Init(String,Project)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectSchemeSetting~Init(String,Project).html) | Initializes object with a project settings node path. |

Exceptions

| Exception | Description |
| --- | --- |
| [BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when scheme with given settings node path can not be found. |

Example

Creating a SchemeSetting object and initializing it with a settings node path

**C#**

```
SchemeSetting oSchemeSetting = new SchemeSetting();

oSchemeSetting.Init("USER.DXF.SCHEMES");

```
