# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Properties.html

---

Exposes P8 properties.

Syntax

**C#**



public new PlacementPropertyList Properties {get;}

public:

new property PlacementPropertyList^ Properties {

   PlacementPropertyList^ get();

}


#### Property Value

PlacementPropertyList: the list of properties of this placement.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown during attempt to access transient placement's properties. |
| [ForbiddenOperationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ForbiddenOperationException.html) | Thrown when this property is used for [Eplan.EplApi.DataModel.EObjects.TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html) or [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html) objects |

Remarks

Do NOT use this function for `TerminalStrip` and `PlugStrip` objects.
