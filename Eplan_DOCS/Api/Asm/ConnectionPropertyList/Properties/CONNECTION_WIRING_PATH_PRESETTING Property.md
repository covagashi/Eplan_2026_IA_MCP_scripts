# CONNECTION_WIRING_PATH_PRESETTING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRING_PATH_PRESETTING().html

---

Layout space: Routing track specification # 31094.

Syntax

**C#**



public PropertyValue CONNECTION_WIRING_PATH_PRESETTING {get; set;}

public:

property PropertyValue^ CONNECTION_WIRING_PATH_PRESETTING {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property stores routing paths and routing ranges that a routed connection in the layout space has to run through. This has priority over all other defaults.

This property is extended in each case to include routing paths and routing ranges to which a connection is pulled. If the connection is pulled away from a routing path or routing range entered here, the routing path / routing range will be removed from the property.
