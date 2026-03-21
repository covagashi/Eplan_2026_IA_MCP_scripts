# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip~Properties.html

---

.NET Property enabling access to P8 properties of the PlugStrip object.

Syntax

**C#**



public new PlugStripPropertyListComplete Properties {get;}

public:

new property PlugStripPropertyListComplete^ Properties {

   PlugStripPropertyListComplete^ get();

}


#### Property Value

P8 properties of the PlugStrip.

Example

**C#**

```
PlugStrip ps;//a valid PlugStrip

ps.Properties[Properties.PlugStrip.DESIGNATION_PLANT] = "AP";

int cnt = ps.Properties[Properties.PlugStrip.PLUGSTRIP_COUNTOFPE];
```
