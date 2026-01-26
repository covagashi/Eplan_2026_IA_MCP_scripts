# TerminalStrip Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal~TerminalStrip.html

---

Returns [TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html) the Terminal belongs to.

Syntax

**C#**



public TerminalStrip TerminalStrip {get;}

public:

property TerminalStrip^ TerminalStrip {

   TerminalStrip^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The [TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html) for this Terminal cannot be found. |
| [Eplan.EplApi.DataModel.WrongCategoryException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.WrongCategoryException.html) | Thrown when the terminal is not related to [TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html), but to a [PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC.html) |
