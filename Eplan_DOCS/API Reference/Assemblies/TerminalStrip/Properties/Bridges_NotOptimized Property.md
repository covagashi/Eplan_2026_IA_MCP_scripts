# Bridges_NotOptimized Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip~Bridges_NotOptimized.html

---

Returns an array of bridge segments groups connected to all terminals of the terminal strip

Syntax

**C#**



public Terminal.Bridge[] Bridges_NotOptimized {get;}

public:

property array<Terminal.Bridge^>^ Bridges_NotOptimized {

   array<Terminal.Bridge^>^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown when the internal interface cannot be initialized |
| [System.NotImplementedException](#) | Thrown when implementation of requested interface isn't found. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal function fails. |

Remarks

The result is the same as iterating through all terminals of the strip and collecting the bridges returned by the [Terminal.Bridges](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal~Bridges.html) property of each terminal. Using this property, however, is more efficient in terms of performance.
