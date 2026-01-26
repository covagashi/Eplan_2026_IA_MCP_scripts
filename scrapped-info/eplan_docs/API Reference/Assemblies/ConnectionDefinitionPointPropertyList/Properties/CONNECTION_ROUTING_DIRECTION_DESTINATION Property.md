# CONNECTION_ROUTING_DIRECTION_DESTINATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic120.html

---

Routing direction target # 31115.

Syntax

**C#**



public PropertyValue CONNECTION_ROUTING_DIRECTION_DESTINATION {get; set;}

public:

property PropertyValue^ CONNECTION_ROUTING_DIRECTION_DESTINATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

The routing directions are defined automatically on the basis of the implemented routing of the connection. They reflect the direction of the routing of the wire from the devices to the routing track.
