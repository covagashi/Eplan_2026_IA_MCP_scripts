# TerminalAccessories Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip~TerminalAccessories.html

---

Returns all [TerminalAccessory](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalAccessory.html) assigned to the terminal strip.

Syntax

**C#**



public TerminalAccessory[] TerminalAccessories {get;}

public:

property array<TerminalAccessory^>^ TerminalAccessories {

   array<TerminalAccessory^>^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the information cannot be read from the project. |
