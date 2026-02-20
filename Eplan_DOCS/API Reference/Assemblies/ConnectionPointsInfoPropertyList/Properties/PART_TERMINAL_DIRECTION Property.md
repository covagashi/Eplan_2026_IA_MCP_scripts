# PART_TERMINAL_DIRECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_TERMINAL_DIRECTION().html

---

Routing direction (default) # 22948.

Syntax

**C#**



public PropertyValue PART_TERMINAL_DIRECTION {get; set;}

public:

property PropertyValue^ PART_TERMINAL_DIRECTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is used if no routing direction has been entered for the individual connection point in the connection point pattern. The property is entered in parts management for connection point patterns and specifies the default value of the routing direction for a group of connection points.

0 = Automatic

1 = Move up

2 = Down

3 = Left

4 = Right.
