# CONNECTION_CABLING_PATH_PRESETTING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_CABLING_PATH_PRESETTING().html

---

Topology: Routing track specification # 31119.

Syntax

**C#**



public PropertyValue CONNECTION_CABLING_PATH_PRESETTING {get; set;}

public:

property PropertyValue^ CONNECTION_CABLING_PATH_PRESETTING {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

In this property, a routing path is stored that a connection routed in the routing path network must pass through. This has priority over all other defaults.

Here, it is always the last routing path to which a connection is drawn that is stored. If the connection is pulled away from the routing path entered here, the routing path will be removed from the property.
