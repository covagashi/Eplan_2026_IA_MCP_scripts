# CONNECTION_TERMINAL_CONNECTIONDESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_TERMINAL_CONNECTIONDESIGNATION().html

---

Connection: Associated terminal connection point (connection point designation) # 31118.

Syntax

**C#**



public PropertyValue CONNECTION_TERMINAL_CONNECTIONDESIGNATION {get; set;}

public:

property PropertyValue^ CONNECTION_TERMINAL_CONNECTIONDESIGNATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

This property can be used in terminal diagrams in the data area of the cable chart (via the placeholder elements "Cable chart data area external" and "Cable chart data area internal"). Indicates the connection point designation of the terminal to which the connection is connected. Thus, you can see from the cable chart which connection is to be connected to which terminal connection point. For example, this is helpful if you use the placeholder elements "Target via connection point", "Connection via connection point" or "Connection / cable via connection point" to output several terminal connection points in a row.
