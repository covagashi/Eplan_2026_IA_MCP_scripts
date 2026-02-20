# SubTerminals Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal~SubTerminals.html

---

If this terminal is the main part of a multi-level terminal, this property returns other parts of the multi-level terminal. Otherwise, an empty array is returned.

Syntax

**C#**



public Terminal[] SubTerminals {get;}

public:

property array<Terminal^>^ SubTerminals {

   array<Terminal^>^ get();

}


Remarks

Note: Accessing this property may be time consuming in case of main terminals existing on large terminal strips. Consider usage of the [Terminal.TerminalStripCache](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+TerminalStripCache.html) object when accessing this property multiple times on terminals of the same strip.
