# PotentialDefinitions Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~PotentialDefinitions.html

---

Returns the [PotentialDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinition.html) related to this connection.

Syntax

**C#**



public PotentialDefinition[] PotentialDefinitions {get;}

public:

property array<PotentialDefinition^>^ PotentialDefinitions {

   array<PotentialDefinition^>^ get();

}


#### Property Value

An array of [PotentialDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinition.html)s related to this connection.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it is impossible to read PotentialDefinitions. |
