# ToTime Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToTime.html

---

Converts this MDPropertyValue object to `System::DateTime`.

Syntax

**C#**



public DateTime ToTime()

public:

DateTime ToTime();


#### Return Value

`System::DateTime` value of the MDPropertyValue.

Exceptions

| Exception | Description |
| --- | --- |
| [MDInvalidTimeValueException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDInvalidTimeValueException.html) | Thrown when property value isn't a valid time value. |
