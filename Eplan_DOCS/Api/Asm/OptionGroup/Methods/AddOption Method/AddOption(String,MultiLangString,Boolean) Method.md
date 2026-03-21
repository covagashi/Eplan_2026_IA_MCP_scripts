# AddOption(String,MultiLangString,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup~AddOption(String,MultiLangString,Boolean).html

---

Adds [Option](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Option.html) to the OptionGroup.

Syntax

**C#**



public Option AddOption( 

   string strName,

   MultiLangString mlDescription,

   bool bIsActive

)

public:

Option^ AddOption( 

   String^ strName,

   MultiLangString^ mlDescription,

   bool bIsActive

)


#### Parameters

*strName*
:   name of the option

*mlDescription*
:   multilang description of the option

*bIsActive*
:   state of the option

#### Return Value

Returns added Option.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strName` is `null`. |
| [System.ArgumentException](#) | Thrown when `strName` is `empty`. |
| [System.ArgumentException](#) | Thrown when `mlDescription` is `empty`. |
| [System.ArgumentException](#) | Thrown when `Option` with `strName` already exists in OptionGroup. |
