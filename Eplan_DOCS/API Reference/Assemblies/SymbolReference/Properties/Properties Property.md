# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~Properties.html

---

EPLAN properties of the SymbolReference object.

Syntax

**C#**



public new SymbolReferencePropertyList Properties {get;}

public:

new property SymbolReferencePropertyList^ Properties {

   SymbolReferencePropertyList^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) | Thrown when this property is used on [Eplan.EplApi.DataModel.EObjects.TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html) or [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html) objects. |

Remarks

Do NOT use this class member on `TerminalStrip` and `PlugStrip` objects.
