# Terminals Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip~Terminals.html

---

Returns all [Terminal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal.html) of the terminal strip.

Syntax

**C#**



public Terminal[] Terminals {get;}

public:

property array<Terminal^>^ Terminals {

   array<Terminal^>^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when terminals of the terminal strip cannot be read from the project. |
