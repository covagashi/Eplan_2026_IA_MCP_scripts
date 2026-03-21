# Bridges_Split Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip~Bridges_Split.html

---

Returns an array of all bridges connected to terminals of the terminal strip.

Syntax

**C#**



public Terminal.Bridge[] Bridges_Split {get;}

public:

property array<Terminal.Bridge^>^ Bridges_Split {

   array<Terminal.Bridge^>^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown when the internal interface cannot be initialized |
| [System.NotImplementedException](#) | Thrown when implementation of requested interface isn't found. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal function fails. |

Remarks

This property returns similar result as the [Bridges](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip~Bridges.html) property, but 'vertical' and 'horizontal' bridges are returned separately. 'Vertical' bridge is a bridge that connects parts of one multi-level terminal. 'Horizontal' bridge is a bridge that connects different multi-level terminals (or just different terminals in case of single level terminals).
