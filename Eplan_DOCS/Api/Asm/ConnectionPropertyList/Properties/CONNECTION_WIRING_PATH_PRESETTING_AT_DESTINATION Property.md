# CONNECTION_WIRING_PATH_PRESETTING_AT_DESTINATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic137.html

---

Layout space: Specification for entry into routing path network (target) # 31116.

Syntax

**C#**



public PropertyValue CONNECTION_WIRING_PATH_PRESETTING_AT_DESTINATION {get; set;}

public:

property PropertyValue^ CONNECTION_WIRING_PATH_PRESETTING_AT_DESTINATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Displays the DT of the channel or routing path through which the connection is to exit the routing path network toward the target item. The property is filled upon the manual definition of the entry into the routing path network.
