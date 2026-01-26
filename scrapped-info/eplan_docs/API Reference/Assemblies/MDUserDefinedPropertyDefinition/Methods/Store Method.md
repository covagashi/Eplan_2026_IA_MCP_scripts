# Store Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDUserDefinedPropertyDefinition~Store.html

---

Stores property definition to the database.

Syntax

**C#**



public bool Store()

public:

bool Store();


Remarks

MDUserDefinedPropertyDefinition is a `transient` (also called "`offline`") object. This means that its properties are initialized once during creation and not updated after every change in database. For this reason, this method must be called after object modification so that the changes are transferred to the parts database.
