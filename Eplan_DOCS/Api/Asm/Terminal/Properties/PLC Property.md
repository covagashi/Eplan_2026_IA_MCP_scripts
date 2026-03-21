# PLC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal~PLC.html

---

Returns [PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC.html) the Terminal belongs to.

Syntax

**C#**



public PLC PLC {get;}

public:

property PLC^ PLC {

   PLC^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The [PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC.html) for this Terminal cannot be found. |
| [Eplan.EplApi.DataModel.WrongCategoryException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.WrongCategoryException.html) | Thrown when the terminal is not related to [PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC.html), but to a [TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html) |
