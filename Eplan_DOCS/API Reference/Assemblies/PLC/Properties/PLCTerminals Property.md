# PLCTerminals Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC~PLCTerminals.html

---

\Returns all [Terminal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal.html)s assigned to the PLC.

Syntax

**C#**



public Terminal[] PLCTerminals {get;}

public:

property array<Terminal^>^ PLCTerminals {

   array<Terminal^>^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when cannot read [Terminal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal.html)s assigned to this PLC. |
