# Init Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.SchemeSetting~Init.html

---

Initializes object with a settings node path.

Syntax

**C#**



public virtual void Init( 

   string strScheme

)

public:

virtual void Init( 

   String^ strScheme

)


#### Parameters

*strScheme*
:   Path to the settings node, for example USER.DXF.SCHEMES

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
