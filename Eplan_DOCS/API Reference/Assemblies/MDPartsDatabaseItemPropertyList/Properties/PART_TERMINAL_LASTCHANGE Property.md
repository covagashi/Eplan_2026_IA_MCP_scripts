# PART_TERMINAL_LASTCHANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~PART_TERMINAL_LASTCHANGE().html

---

Last editor / Modification date (connection point pattern) # 22944.

Syntax

**C#**



public MDPropertyValue PART_TERMINAL_LASTCHANGE {get; set;}

public:

property MDPropertyValue^ PART_TERMINAL_LASTCHANGE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Last change to the connection point pattern in parts management. Shows the sign-in name of the user who last edited the record along with the date and time of the last change. The time is output in the local time of the user in accordance with the set time zone.
