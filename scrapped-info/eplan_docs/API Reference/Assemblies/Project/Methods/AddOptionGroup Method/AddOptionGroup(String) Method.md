# AddOptionGroup(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~AddOptionGroup(String).html

---

Adds [OptionGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup.html) to the `Project`. The description is set to an empty multilang value.

Syntax

**C#**



public OptionGroup AddOptionGroup( 

   string strName

)

public:

OptionGroup^ AddOptionGroup( 

   String^ strName

)


#### Parameters

*strName*
:   name of the option

#### Return Value

Returns added Option.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strName` is `null`. |
| [System.ArgumentException](#) | Thrown when `strName` is `empty`. |
| [System.ArgumentException](#) | Thrown when `OptionGroup` with `strName` already exists in Project. |

Remarks

Option name must be unique for the `Project`.
