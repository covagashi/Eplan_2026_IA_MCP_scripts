# Options Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~Options.html

---

Returns array of [Option](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Option.html)s assigned to the `Project` but not those that are assigned to OptionGroups.

Syntax

**C#**



public Option[] Options {get;}

public:

property array<Option^>^ Options {

   array<Option^>^ get();

}


#### Property Value

Array of [OptionGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionGroup.html)s assigned to the `Project`.
