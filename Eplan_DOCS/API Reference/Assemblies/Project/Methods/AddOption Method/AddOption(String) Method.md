# AddOption(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~AddOption(String).html

---

Adds [Option](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Option.html) to the `Project`.

Syntax

**C#**



public Option AddOption( 

   string strName

)

public:

Option^ AddOption( 

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
| [System.ArgumentException](#) | Thrown when `Option` with `strName` already exists in Project. |

Remarks

This method adds an `Option` straight to the `Project`, Option is not assigned to any `OptionGroup`. Option name must be unique in the set of Options that are not assigned to any `OptionGroup`.
