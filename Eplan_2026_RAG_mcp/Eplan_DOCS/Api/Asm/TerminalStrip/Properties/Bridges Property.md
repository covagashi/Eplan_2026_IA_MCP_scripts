# Bridges Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip~Bridges.html

---

Returns an array of all bridges connected to terminals of the terminal strip.

Syntax

**C#**



public Terminal.Bridge[] Bridges {get;}

public:

property array<Terminal.Bridge^>^ Bridges {

   array<Terminal.Bridge^>^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown when the internal interface cannot be initialized |
| [System.NotImplementedException](#) | Thrown when implementation of requested interface isn't found. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal function fails. |

Remarks

Bridge segments of the same kind and type which connect at least one common terminal are grouped together and are returned as one bridge with many segments. (Note: a segment represents two terminals connected by a single bridge connection.)
