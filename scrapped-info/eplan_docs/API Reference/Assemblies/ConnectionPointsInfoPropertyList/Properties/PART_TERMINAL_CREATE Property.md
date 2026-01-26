# PART_TERMINAL_CREATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_TERMINAL_CREATE().html

---

Creator / Creation date (connection point pattern) # 22943.

Syntax

**C#**



public PropertyValue PART_TERMINAL_CREATE {get; set;}

public:

property PropertyValue^ PART_TERMINAL_CREATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Creation date of the connection point pattern. The time is output in the local time of the user in accordance with the set time zone.
