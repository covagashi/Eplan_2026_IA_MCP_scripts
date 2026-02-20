# GetNextEmbeddedInstance Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DynamicConnectionLine~GetNextEmbeddedInstance.html

---

Returns next instance embedded in this line after one given as a parameter.

Syntax

**C#**



public Placement GetNextEmbeddedInstance( 

   Placement placement

)

public:

Placement^ GetNextEmbeddedInstance( 

   Placement^ placement

)


#### Parameters

*placement*
:   [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) before returned placement.

#### Return Value

`null` when there is no more instances embedded

next embedded instance

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the next embedded instance cannot be read. |
| [System.ArgumentNullException](#) | Thrown when `placement` is `null`. |
