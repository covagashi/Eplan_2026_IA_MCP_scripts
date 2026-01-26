# MergedObjects Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnection~MergedObjects.html

---

Returns an array of [Connection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection.html)s covered by this merged connection.

Syntax

**C#**



public Connection[] MergedObjects {get;}

public:

property array<Connection^>^ MergedObjects {

   array<Connection^>^ get();

}


#### Property Value

An array of objects covered by this merged connection

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when object wasn't created. |
