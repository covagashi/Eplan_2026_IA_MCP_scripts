# PART_TERMINAL_DIRECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~PART_TERMINAL_DIRECTION().html

---

Routing direction (default) # 22948.

Syntax

**C#**



public MDPropertyValue PART_TERMINAL_DIRECTION {get; set;}

public:

property MDPropertyValue^ PART_TERMINAL_DIRECTION {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

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
