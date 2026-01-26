# Bridges Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal~Bridges.html

---

This property returns information about all [Terminal.Bridge](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge.html) attached to the terminal. If this terminal is a single terminal and if it has any bridges attached, one item is returned in the array. This item contains all the bridge segments which are attached to the terminal. (Note: a segment represents two terminals connected by a single bridge connection.) If this terminal is a part of a multi-level terminal (i.e. group of terminals being one article on the terminal strip), the array of more than one items may be returned. Each of the items returned contains segments attached to an individual terminal (i.e. one level) of the multi-level terminal.

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
| [System.InvalidOperationException](#) | Thrown when interface cannot be initialized or it cannot return functions. Also thrown for PLC terminals. |
| [System.NotImplementedException](#) | Thrown when implementation of requested interface isn't found. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal function fails. |

Remarks

\* Elements returned by this property are not bridges actually, but rather groups of bridge segments connected directly to one individual terminal. Segments in one such group doesn't have to be of equal type and kind. \* This property is not valid for PLC terminals.
