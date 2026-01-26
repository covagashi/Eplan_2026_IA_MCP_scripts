# ToTime Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~ToTime.html

---

Used in conversion of the PropertyValue object to `time`.

Syntax

**C#**



public DateTime ToTime()

public:

DateTime ToTime();


#### Return Value

Time value of the PropertyValue.

Exceptions

| Exception | Description |
| --- | --- |
| [InvalidTimeValueException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidTimeValueException.html) | Throws when property value isn't valid time value. |
