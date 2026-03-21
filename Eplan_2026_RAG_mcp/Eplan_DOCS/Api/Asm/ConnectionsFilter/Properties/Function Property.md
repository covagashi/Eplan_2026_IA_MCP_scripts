# Function Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionsFilter~Function.html

---

Sets the [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) that [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s matching the filter must have as the start or the end function.

Syntax

**C#**



public Function Function {get; set;}

public:

property Function^ Function {

   Function^ get();

   void set (    Function^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
