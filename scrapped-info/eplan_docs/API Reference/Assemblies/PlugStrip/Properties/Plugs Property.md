# Plugs Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip~Plugs.html

---

Returns all [Plug](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Plug.html) objects of the plug strip.

Syntax

**C#**



public Plug[] Plugs {get;}

public:

property array<Plug^>^ Plugs {

   array<Plug^>^ get();

}


Remarks

In case the whole connector contains two sides (i.e. pin-side and socket-side) this property returns plugs whose side corresponds to the side of the plug strip only.
