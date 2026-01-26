# CONNECTION_WIRING_PATH_PRESETTING_AT_SOURCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_WIRING_PATH_PRESETTING_AT_SOURCE().html

---

Layout space: Specification for entry into routing path network (source) # 31100.

Syntax

**C#**



public PropertyValue CONNECTION_WIRING_PATH_PRESETTING_AT_SOURCE {get; set;}

public:

property PropertyValue^ CONNECTION_WIRING_PATH_PRESETTING_AT_SOURCE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Displays the DT of the channel or routing path through which the connection is to enter the routing path network from the source item. The property is filled upon the manual definition of the entry into the routing path network.
