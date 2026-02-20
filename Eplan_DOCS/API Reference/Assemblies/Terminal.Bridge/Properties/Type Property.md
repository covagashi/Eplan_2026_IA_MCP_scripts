# Type Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge~Type.html

---

A type of the bridge. Corresponds to the function definition tag of the bridge's connections.

Syntax

**C#**



public int Type {get;}

public:

property int Type {

   int get();

}


Remarks

Note: if the bridge contains segments of many types, the type of the bridge itself is undetermined (the property returns -1).
