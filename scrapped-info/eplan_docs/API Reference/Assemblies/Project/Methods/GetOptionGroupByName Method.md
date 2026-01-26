# GetOptionGroupByName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~GetOptionGroupByName.html

---

Method for finding [OptionGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup.html) assigned to the `Project` with a given name.

Syntax

**C#**



public OptionGroup GetOptionGroupByName( 

   string strName

)

public:

OptionGroup^ GetOptionGroupByName( 

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
