# AddOptionGroup(String,MultiLangString) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~AddOptionGroup(String,MultiLangString).html

---

Adds [OptionGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup.html) to the `Project`. The description is set to default multilang value.

Syntax

**C#**



public OptionGroup AddOptionGroup( 

   string strName,

   MultiLangString mlDescription

)

public:

OptionGroup^ AddOptionGroup( 

   String^ strName,

   MultiLangString^ mlDescription

)


#### Parameters

*strName*
:   name of the option

*mlDescription*

#### Return Value

Returns added Option.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strName` is `null`. |
| [System.ArgumentException](#) | Thrown when `strName` is `empty`. |
| [System.ArgumentException](#) | Thrown when `OptionGroup` with `strName` already exists in Project. |
