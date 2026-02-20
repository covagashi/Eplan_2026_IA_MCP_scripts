# IsVertical Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge~IsVertical.html

---

Returns information whether the bridge is 'vertical', i.e. whether it connects only different levels of the same multi-level terminal. Note: this property is valid only if the bridge object has been obtained through the TerminalStrip.Bridges\_Split property of a terminal strip object. Otherwise, this property returns FALSE.

Syntax

**C#**



public bool IsVertical {get;}

public:

property bool IsVertical {

   bool get();

}

