# GetOptionByName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~GetOptionByName.html

---

Method for finding [Option](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Option.html) assigned to the `Project` with a given name.

Syntax

**C#**



public Option GetOptionByName( 

   string strName

)

public:

Option^ GetOptionByName( 

   String^ strName

)


#### Parameters

*strName*
:   name of the OptionGroup

#### Return Value

[OptionGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup.html) assigned to the `Project` with a given name.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strName` is `null`. |
| [System.ArgumentException](#) | Thrown when `strName` is `empty`. |

Remarks

Searches only among the options that are not assigned to OptionGroups. For options assigned to OptionGroup: get the OptionGroup and use OptionGroup's `Option ^ GetOptionByName(System::String ^ strName)`.
