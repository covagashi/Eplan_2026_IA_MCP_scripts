# Load Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDUserDefinedPropertyDefinition~Load().html

---

Loads property definition from the database.

Syntax

**C#**



public bool Load()

public:

bool Load();


Remarks

MDUserDefinedPropertyDefinition is a `transient` (also called "`offline`") object. This means that its properties are initialized once during creation and not updated after every change in database. For this reason, this method must be called to keep the object up to date with the parts database.
